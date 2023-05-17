import type { Options, OptionsFunc } from "@/components/AppSelectTags.vue";
import { stringify } from "@/util/object";
import { biolink, request } from "./";
import { getSearchResults } from "./search";

/** search individual phenotypes or gene/disease phenotypes */
export const getPhenotypes = async (search = ""): ReturnType<OptionsFunc> => {
  /**
   * detect pasted list of phenotype ids. deliberately don't detect single id.
   * handle that with regular search.
   */
  const ids = search.split(/\s*,\s*/);
  if (ids.length >= 2)
    return {
      autoAccept: true,
      options: ids.map((id) => ({ id })),
      message: ids.every((id) => id.startsWith("HP:"))
        ? ""
        : 'One or more pasted IDs were not valid HPO phenotype IDs (starting with "HP:")',
    };

  /** otherwise perform string search for phenotypes/genes/diseases */
  const { items } = await getSearchResults(search, 0, 20, {
    category: ["phenotype", "gene", "disease"],
  });

  /** convert into desired result format */
  return {
    options: items.map((item) => ({
      id: item.id,
      name: item.name,
      spreadOptions:
        /**
         * if gene/disease, provide function to get associated phenotypes upon
         * select
         */
        item.category === "phenotype" || !item.category
          ? undefined
          : async () => await getPhenotypeAssociations(item.id, item.category),
      highlight: item.highlight,
      icon: "category-" + item.category,
      info: item.in_taxon || "",
    })),
  };
};

/** phenotype associations with gene/disease (from backend) */
type _PhenotypeAssociations = {
  associations: {
    object: {
      id: string;
      label: string;
    };
  }[];
};

/** get phenotypes associated with gene/disease */
const getPhenotypeAssociations = async (
  id = "",
  category = ""
): Promise<Options> => {
  /** short circuit if no id or valid category */
  if (!id || !category || !(category === "gene" || category === "disease"))
    throw new Error(`Invalid gene/disease id or category`);

  /** endpoint settings */
  const params = {
    direct: true,
    unselect_evidence: true,
  };

  /** make query */
  const url = `${biolink}/bioentity/${category}/${id}/phenotypes`;
  const { associations } = await request<_PhenotypeAssociations>(url, params);

  /** convert into desired result format */
  return associations.map(({ object }) => ({
    id: object.id,
    name: object.label,
  }));
};

/** results of phenotype comparison (from backend) */
type _Comparison = {
  matches: {
    id: string;
    label: string;
    type: string;
    taxon?: {
      id?: string;
      label?: string;
    };
    rank: string;
    score: number;
    significance: string;
  }[];
};

/** compare a set of phenotypes to another set of phenotypes */
export const compareSetToSet = async (
  aPhenotypes: string[],
  bPhenotypes: string[]
): Promise<Comparison> => {
  /** make request options */
  const headers = new Headers();
  headers.append("Content-Type", "application/json");
  headers.append("Accept", "application/json");
  const body = {
    reference_ids: aPhenotypes,
    query_ids: [bPhenotypes],
    is_feature_set: aPhenotypes.every((id) => id.startsWith("HP:")),
  };
  const options = {
    method: "POST",
    headers,
    body: stringify(body),
  };

  /** make query */
  const url = `${biolink}/sim/compare`;
  const response = await request<_Comparison>(url, {}, options);

  return mapMatches(response);
};

/** compare a set of phenotypes to a gene or disease taxon id */
export const compareSetToTaxon = async (
  phenotypes: string[],
  taxon: string
): Promise<Comparison> => {
  /** endpoint settings */
  const params = {
    id: phenotypes,
    taxon: taxon,
  };

  /** make query */
  const url = `${biolink}/sim/search`;
  const response = await request<_Comparison>(url, params);

  return mapMatches(response);
};

/** convert comparison matches into desired result format */
const mapMatches = (response: _Comparison) => {
  const matches = response.matches.map((match) => ({
    id: match.id,
    name: match.label,
    score: match.score,
    category: match.type || "phenotype",
    taxon: match.taxon?.label || "",
  }));
  const minScore = Math.min(...matches.map(({ score }) => score));
  const maxScore = Math.max(...matches.map(({ score }) => score));

  return { matches, minScore, maxScore };
};

/** results of phenotype comparison (for frontend) */
export type Comparison = {
  matches: {
    id: string;
    name: string;
    score: number;
    category: string;
    taxon: string;
  }[];
  minScore?: number;
  maxScore?: number;
};
