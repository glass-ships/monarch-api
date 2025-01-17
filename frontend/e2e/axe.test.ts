import { configureAxe, getViolations, injectAxe } from "axe-playwright";
import { expect, test } from "@playwright/test";
import { log } from "../playwright.config";

log();

/** pages to test */
const paths = [
  "/",
  "/explore#search",
  "/explore#text-annotator",
  "/explore#phenotype-explorer",
  "/about",
  "/help",
  "/cite",
  "/team",
  "/publications",
  "/terms",
  "/feedback",
  "/MONDO:0007523",
  "/testbed",
];

/** axe rule overrides */
const rules = [
  /**
   * axe doesn't like light gray secondary text. also, color standards are not
   * always correct:
   *
   * https://uxmovement.com/buttons/the-myths-of-color-contrast-accessibility/
   * https://github.com/w3c/wcag/issues/695
   * https://twitter.com/DanHollick/status/1468958644364402702
   * https://github.com/Myndex/SAPC-APCA
   * https://twitter.com/DanHollick/status/1417895151003865090
   * https://twitter.com/argyleink/status/1329091518032867328
   */
  { id: "color-contrast", enabled: false },
  /** ignore select dropdowns that are appended to body */
  { id: "region", selector: ":not([role='listbox']" },
];

/** Reusable test for each page */
const checkPage = (title: string, path: string, selector?: string) =>
  test(title, async ({ page, browserName }) => {
    test.skip(browserName !== "chromium", "Only test Axe on chromium");

    /** navigate to page */
    await page.goto(path);

    /** wait for content to load */
    await page.waitForSelector("main");
    await page.waitForSelector("section");
    await page.waitForSelector("h1");
    await page.waitForTimeout(1000);

    /** setup axe */
    await injectAxe(page);
    await configureAxe(page, { rules });

    /** perform interaction on selector */
    if (selector) {
      await page.locator(selector).first().focus();
      await page.locator(selector).first().click();
    }

    /** axe check */
    const violations = await getViolations(page);
    const violationsMessage = JSON.stringify(violations, null, 2);
    expect(violationsMessage).toBe("[]");
  });

for (const path of paths) checkPage("Accessibility check " + path, path);

checkPage(
  "Accessibility check /testbed (select single)",
  "/testbed",
  ".select-single button",
);
checkPage(
  "Accessibility check /testbed (select multi)",
  "/testbed",
  ".select-multi button",
);
checkPage(
  "Accessibility check /testbed (select tags)",
  "/testbed",
  ".select-tags input",
);
checkPage(
  "Accessibility check /testbed (select autocomplete)",
  "/testbed",
  ".select-autocomplete input",
);
