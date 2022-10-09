import { lazy } from "react";

const TablesRoutes = [
  {
    path: "/tables/reactstrap",
    component: lazy(() => import("../../views/tables/reactstrap")),
  },
  {
    path: "/datatables/basic",
    component: lazy(() => import("../../views/tables/data-tables/basic")),
  },
  {
    path: "/datatables/badgeTable",
    component: lazy(() => import("../../views/tables/data-tables/badgetable")),
  },
  {
    path: "/datatables/badgeUpload",
    component: lazy(() => import("../../views/tables/data-tables/badgeUpload")),
  }
  ,
  {
    path: "/datatables/badgeContentCriteria",
    component: lazy(() => import("../../views/tables/data-tables/badgeContentCriteria")),
  }
  // {
  //   path: '/datatables/advance',
  //   component: lazy(() => import('../../views/tables/data-tables/advance'))
  // }
];

export default TablesRoutes;
