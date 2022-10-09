import axios from "axios";
import img from "../../../assets/images/avatars/xyz.jpg";
import React, {useState} from "react";
export let data;
export let contentsData;
export let BadgeData;
export let BadgeContentData;

axios
  .get(`${process.env.REACT_APP_Base_URL}/api/adminPanel/users/`)
  .then((response) => {
    data = response.data;
  });

let REACT_APP_Base_URL='https://ab-scriptbox.herokuapp.com'  //apply url for images in data sets if online
let REACT_APP_Base_URL2='http://127.0.0.1:8000' //apply url for images in data sets if local

let textArray =[]

const suspendClick = async (id) => {
  const { data } = await axios.post(
      `${process.env.REACT_APP_Base_URL}/api/adminPanel/suspendContent/`,
      {'id':id}
  );
  if (data === "Suspended")
  {
    alert(data)
  }
  else {
    alert("Already Suspended")
  }
};

const applyClick = async (id,i) => {
  const { data } = await axios.post(
      `${process.env.REACT_APP_Base_URL}/api/adminPanel/setBadge/`,
      {'Badgeid':id,'scriptNumber':textArray[i]}
  );

    alert(data)

};
const deleteClick = async (id,i) => {
  const { data } = await axios.delete(
      `${process.env.REACT_APP_Base_URL}/api/adminPanel/deleteBadge/${id}/`,
  );

    alert(data)

};


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
  {
    name: "Action",
    sortable: true,
    minWidth: "175px",
    selector: (row) => {return(
        <button className="btn-sm btn-outline-primary btn-light"
            onClick={(e) => suspendClick(row.id)}

        > Suspend</button>
    )},
  },
  // {
  //   field: 'action4',
  //   headerName: 'Details',
  //   description: 'View Details',
  //   sortable: false,
  //   width: 100,
  //   renderCell: (params) => {
  //     return (
  //         <>
  //           <LinkContainer to={`/order/${params.row.id}`}>
  //             <Button v className='btn-sm theme-btn'>
  //               <InfoSharpIcon fontSize={"small"}/>
  //             </Button>
  //           </LinkContainer>
  //         </>
  //     )
  //   },
  // },

];


axios
    .get(`${process.env.REACT_APP_Base_URL}/api/adminPanel/getBadges/`)
    .then((response) => {
      BadgeData = response.data;
    });

export const badgeColumns = [
  {
    name: "Badge",
    sortable: true,
    minWidth: "100px",
    selector: (row) => {return(
        <>
          <img style={{ height:80,width:80,borderRadius:40,marginRight:10}}
              src={
                REACT_APP_Base_URL2 + row.image
              }
              alt=""
          />
          <label> {row.name}</label>
        </>
    )},
  },
  {
    name: "Description",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.description,
  },
  {
    name: "Apply For Scripts",
    sortable: true,
    minWidth: "175px",
    selector: (row,as) => {return(
        <>
          <input type="text"  style={{width:40}} onChange={(e) => textArray[as]=e.target.value}

          />
        </>
    )},
  },

  {
    name: "Action",
    sortable: true,
    minWidth: "175px",
    selector: (row,i) => {return(
        <button className="btn-sm btn-outline-primary btn-light"
            onClick={(e) => applyClick(row.id,i)}

        > Apply</button>
    )},
  },
]

axios
    .get(`${process.env.REACT_APP_Base_URL}/api/adminPanel/getContentBadges/`)
    .then((response) => {
      BadgeContentData = response.data;
    });
export const badgeContentColumns = [
  {
    name: "Badge",
    sortable: true,
    minWidth: "100px",
    selector: (row) => {return(
        <>
          <img style={{ height:80,width:80,borderRadius:40,marginRight:10}}
               src={
                 REACT_APP_Base_URL2 + row.badge.image
               }
               alt=""
          />
          <label> {row.badge.name}</label>
        </>
    )},
  },
  {
    name: "Description",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.badge.description,
  },
  {
    name: "Number of Scripts",
    sortable: true,
    minWidth: "100px",
    selector: (row) => row.num_script,
  },


  {
    name: "Action",
    sortable: true,
    minWidth: "175px",
    selector: (row,i) => {return(
        <button  className="btn-sm btn-outline-primary btn-light"
            onClick={(e) => deleteClick(row.id,i)}

        > Delete</button>
    )},
  },


]