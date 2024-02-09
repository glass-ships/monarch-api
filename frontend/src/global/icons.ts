import { library } from "@fortawesome/fontawesome-svg-core";
import * as fab from "@fortawesome/free-brands-svg-icons";
import * as far from "@fortawesome/free-regular-svg-icons";
import * as fas from "@fortawesome/free-solid-svg-icons";

/** prefer using "regular" over "solid" where available */

/** create collection/"palette" of useable icons */
const icons = [
  fab.faGithub,
  fab.faLinkedin,
  fab.faMedium,
  fab.faYoutube,
  far.faChartBar,
  far.faCircleCheck,
  far.faCirclePause,
  far.faCircleQuestion,
  far.faCircleXmark,
  far.faClipboard,
  far.faComment,
  far.faComments,
  far.faCopy,
  far.faEnvelope,
  far.faEye,
  far.faFileLines,
  far.faFloppyDisk,
  far.faLightbulb,
  far.faNewspaper,
  far.faPaperPlane,
  far.faSquare,
  fas.faAngleDown,
  fas.faAngleLeft,
  fas.faAngleRight,
  fas.faAnglesLeft,
  fas.faAnglesRight,
  fas.faAngleUp,
  fas.faArrowDown,
  fas.faArrowDownLong,
  fas.faArrowLeft,
  fas.faArrowLeftLong,
  fas.faArrowRight,
  fas.faArrowRightLong,
  fas.faArrowsLeftRight,
  fas.faArrowUp,
  fas.faArrowUpLong,
  fas.faArrowUpRightFromSquare,
  fas.faAsterisk,
  fas.faBarcode,
  fas.faBars,
  fas.faBarsProgress,
  fas.faBook,
  fas.faBullhorn,
  fas.faCheck,
  fas.faCircleExclamation,
  fas.faCircleInfo,
  fas.faClipboardList,
  fas.faClockRotateLeft,
  fas.faCode,
  fas.faCogs,
  fas.faDatabase,
  fas.faDownload,
  fas.faEquals,
  fas.faFeatherPointed,
  fas.faFilter,
  fas.faFlask,
  fas.faHandshakeAngle,
  fas.faLink,
  fas.faLocationDot,
  fas.faMagnifyingGlass,
  fas.faMaximize,
  fas.faMinimize,
  fas.faNotesMedical,
  fas.faPersonRunning,
  fas.faScaleBalanced,
  fas.faShareNodes,
  fas.faSitemap,
  fas.faSquareCheck,
  fas.faSubscript,
  fas.faTable,
  fas.faUpload,
  fas.faUsers,
  fas.faXmark,
];

library.add(...icons);
