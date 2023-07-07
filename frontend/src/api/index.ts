/** base api url */
export const biolink = "https://api.monarchinitiative.org/api";
export const monarch =
  import.meta.env.MONARCH_API || "https://api-dev.monarchinitiative.org/v3/api";

/** environment mode */
const mode = import.meta.env.MODE;

/**
 * key/value object for request query parameters. use primitive for single, e.g.
 * evidence=true. use array for multiple/duplicate, e.g. id=abc&id=def&id=ghi
 */
type Param = string | number | boolean | undefined | null;
export type Params = { [key: string]: Param | Param[] };

/**
 * generic fetch request wrapper
 *
 * @param path request url
 * @param params url params. { param: [1,2,3] } becomes ?param=1&param=2&param=3
 *   { param: "1,2,3" } stays ?param=1,2,3
 * @param options fetch() options
 * @param parse parse response mode
 */
export const request = async <Response>(
  path = "",
  params: Params = {},
  options: RequestInit = {},
  parse: "text" | "json" = "json"
): Promise<Response> => {
  /** start cache if not already started */
  if (!cache) await initCache();

  /** get string of url parameters/options */
  const paramsObject = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    const values = [value].flat();
    for (const value of values)
      if (["string", "number", "boolean"].includes(typeof value))
        paramsObject.append(key, String(value));
  }

  /** sort params for consistency */
  paramsObject.sort();

  /** assemble url to query */
  const paramsString = "?" + paramsObject.toString();
  const url = path + paramsString;

  /** endpoint for logging */
  let endpoint = path;
  if (endpoint.startsWith(biolink))
    endpoint = endpoint.replace(biolink, "biolink ");
  if (endpoint.startsWith(monarch))
    endpoint = endpoint.replace(monarch, "monarch ");

  /** make request object */
  const request = new Request(url, options);

  /** first check if request is cached */
  let response = await cache.match(request);

  /** log details for debugging (except don't clutter logs when running tests) */
  if (mode !== "test") {
    console.groupCollapsed(
      response ? "📞 Request (cached)" : "📞 Request (new)",
      endpoint
    );
    console.info("Url", url);
    console.info("Params", params);
    console.info("Options", options);
    console.info("Request", request);
    console.groupEnd();
  }

  /** if request not cached */
  if (!response) {
    /** make new request */
    response = await fetch(url, options);

    /** check response code */
    if (!response.ok) {
      /** get biolink error message, if there is one */
      let message;
      try {
        message = ((await response.json()) as _Error).error.message;
      } catch (error) {
        message = "";
      }
      throw new Error(message || `Response not OK`);
    }

    /**
     * add response to cache (if GET,
     * https://w3c.github.io/ServiceWorker/#cache-put)
     */
    if (request.method === "GET") await cache.put(request, response.clone());
  }

  /** parse response */
  const parsed =
    parse === "text"
      ? ((await response.text()) as unknown as Response)
      : await response.json();

  /** log details for debugging (except don't clutter logs when running tests) */
  if (mode !== "test") {
    console.groupCollapsed("📣 Response", endpoint);
    console.info("Url", url);
    console.info("Parsed", parsed);
    console.info("Response", response);
    console.groupEnd();
  }

  return parsed;
};

/** cache interface */
let cache: Cache;
const name = "monarch-cache";

/** start cache */
const initCache = async () => {
  /** start fresh each session (as if using sessionStorage) */
  await window.caches.delete(name);
  /** set cache interface */
  cache = await window.caches.open(name);
};

/** possible biolink error */
type _Error = {
  error: {
    message: string;
  };
};

/**
 * create dummy caches interface. only really needed for local mobile testing so
 * requests don't error.
 * https://stackoverflow.com/questions/53094298/window-caches-is-undefined-in-android-chrome-but-is-available-at-desktop-chrome
 */
if (!window.caches) {
  window.caches = {
    open: async () => ({
      match: (async () => undefined) as Cache["match"],
      put: (async () => undefined) as Cache["put"],
    }),
    delete: (async () => true) as CacheStorage["delete"],
  } as unknown as CacheStorage;
}
