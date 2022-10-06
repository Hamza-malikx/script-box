import axios from "axios";
export let data;
export let contentsData;

axios
  .get(`${process.env.REACT_APP_Base_URL}/api/adminPanel/users/`)
  .then((response) => {
    data = response.data;
  });

export const userColumns = [
  {
    name: "ID",
    sortable: true,
    maxWidth: "100px",
    selector: (row) => row.id,
  },
  {
    name: "Email",
    sortable: true,
    minWidth: "310px",
    selector: (row) => row.email,
  },
  {
    name: "Username",
    sortable: true,
    minWidth: "250px",
    selector: (row) => row.username,
  },
  {
    name: "Role",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.role,
  },
  {
    name: "Last Login",
    sortable: true,
    minWidth: "225px",
    selector: (row) => row.last_login,
  },
  {
    name: "Date joined",
    sortable: true,
    minWidth: "175px",
    selector: (row) => row.date_joined,
  },
];

axios
  .get(`${process.env.REACT_APP_Base_URL}/api/user/allContent/`)
  .then((response) => {
    contentsData = response.data;
  });

export const contentsColumns = [
  {
    name: "Title",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.title,
  },
  {
    name: "User",
    sortable: true,
    maxWidth: "100px",
    selector: (row) => row.user,
  },
  {
    name: "views",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.views,
  },
  {
    name: "type",
    sortable: true,
    minWidth: "225px",
    selector: (row) => row.type,
  },
  {
    name: "tag",
    sortable: true,
    minWidth: "225px",
    selector: (row) => row.tag,
  },
  {
    name: "privacy",
    sortable: true,
    minWidth: "225px",
    selector: (row) => row.privacy,
  },
  {
    name: "rating",
    sortable: true,
    minWidth: "225px",
    selector: (row) => row.rating,
  },
  {
    name: "is_verified",
    sortable: true,
    minWidth: "225px",
    selector: (row) => (row.is_verified === false ? "False" : "True"),
  },
  {
    name: "is_universal",
    sortable: true,
    minWidth: "225px",
    selector: (row) => (row.is_universal === false ? "False" : "True"),
  },
  {
    name: "created_at",
    sortable: true,
    minWidth: "175px",
    selector: (row) => row.created_at,
  },
];
