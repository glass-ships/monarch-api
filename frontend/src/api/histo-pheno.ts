import { sortBy } from "lodash";
import { biolink, request } from "./index";

/** histopheno data (from backend) */
interface _HistoPheno {
  facet_counts: {
    object_closure: Record<string, number>;
    closure_bin: Record<string, number>;
  };
}

/** histopheno data (for frontend) */
type Histogram = Array<{
  id: string;
  name: string;
  count: number;
}>;

/** get data for histopheno (node page visualization of phenotypes for disease) */
export const getHistoPheno = async (disease: string): Promise<Histogram> => {
  const params = {
    rows: 0,
    facet: true,
    unselect_evidence: false,
    exclude_automatic_assertions: false,
    fetch_objects: false,
    use_compact_associations: false,
    direct: false,
    direct_taxon: false,
  };

  const url = `${biolink}/bioentity/disease/${disease}/phenotypes`;

  const response = await request<_HistoPheno>(url, params);

  return sortBy(
    Object.entries(response.facet_counts.closure_bin).map(
      ([name, count], index) => ({
        id: Object.keys(response.facet_counts.object_closure)[index],
        name,
        count,
      })
    ),
    "count"
  )
    .filter(({ count }) => count)
    .reverse();
};
