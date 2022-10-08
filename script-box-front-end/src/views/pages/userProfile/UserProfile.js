import React, { useState, useEffect, useCallback } from "react";
import styles from "./userProfile.module.css";
import Header from "../home/navbar/Header";
import avatar from "../../../assets/images/avatars/avatar.png";
import { useHistory } from "react-router-dom";
import axios from "axios";

const UserProfile = () => {
  const [bio, editBio] = useState(false);
  const [username, editUsername] = useState(false);
  const [editPass, setEditPass] = useState(false);
  const [loadSite, setLoadSite] = useState(false);

  const [userData, setUserData] = useState();

  const [userBio, setUserBio] = useState(userData?.bio);
  const [userUsername, setUserUsername] = useState(userData?.username);
  const [userPassword, setUserPassword] = useState(userData?.password);
  const [favoriteC, setFavoriteC] = useState([]);
  const [userDetails, setUserDetails] = useState(
    JSON.parse(localStorage.getItem("userData"))
  );
  const getUserDetails = useCallback(async () => {
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/user/get-user/${userDetails.id}/`;

      var res = await axios.get(api);
      if (res.status === 200) {
        setUserData(res.data);
        console.log("res after 200: ", res);
      }
    } catch (e) {
      console.log(e);
    }
  }, [setUserData]);

  useEffect(() => {
    getUserDetails();
    setLoadSite(false);
  }, [getUserDetails, loadSite]);

  useEffect(() => {
    setUserBio(userData?.bio);
    setUserUsername(userData?.username);
    setUserPassword(userData?.password);
    getFavoriteScripts();
  }, [userData]);

  const updateUserDetailHandler = async () => {
    editBio(false);
    editUsername(false);
    setEditPass(false);

    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    const apiData = {
      bio: userBio,
      username: userUsername,
      password: userPassword,
    };
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/user/update/${userDetails.id}/`;

      var res = await axios.put(api, apiData, config);
      if (res.status === 200) {
        console.log("res after 200: ", res);
      }
    } catch (e) {
      console.log(e);
    }
    setLoadSite(true);
  };

  const history = useHistory();
  const logoutNavigator = () => {
    localStorage.removeItem("userData");
    history.push("/");
    window.location.reload(false);
  };
  const getFavoriteScripts = async () => {
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/user/getFavContent/${userDetails.username}/`;
      console.log("userDetails.username", userDetails.username);
      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      var res = await axios.get(api, config);
      if (res.status === 200) {
        console.log("res after 200: ", res);
        setFavoriteC(res.data);
      }
    } catch (e) {
      console.log(e);
    }
  };
  // useEffect(() => {
  //   getFavoriteScripts();
  // }, []);
  return (
    <div>
      <Header />
      <div className="container">
        <div className={styles.profile}>
          <h2>My Account</h2>
          <div className={styles.avatarWrapper}>
            <img src={avatar} alt="" />
            <div className={styles.editAvatarBtnWrapper}>
              <svg
                width="40"
                height="40"
                viewBox="0 0 40 40"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <circle cx="20" cy="20" r="20" fill="#7367F0"></circle>{" "}
                <path
                  d="M24.4211 11.2938C25.2022 10.5127 26.4685 10.5127 27.2496 11.2938L28.6638 12.708C29.4448 13.4891 29.4448 14.7554 28.6638 15.5364L27.2492 16.951L23.0066 12.7084L24.4211 11.2938Z"
                  fill="white"
                ></path>{" "}
                <path
                  d="M18.0572 26.143L25.8353 18.3649L21.5927 14.1222L13.8145 21.9004L18.0572 26.143Z"
                  fill="white"
                ></path>{" "}
                <path
                  d="M16.6429 27.5572L12.1764 29.0461C11.3946 29.3067 10.6509 28.563 10.9114 27.7812L12.4003 23.3146L16.6429 27.5572Z"
                  fill="white"
                ></path>
              </svg>
            </div>
          </div>
          <div className={styles.verifiedBadge}>
            <span>Verified</span>
            <svg
              width="12"
              height="16"
              viewBox="0 0 17 20"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M8.18182 0L0 3.63636V9.09091C0 14.1364 3.49091 18.8545 8.18182 20C12.8727 18.8545 16.3636 14.1364 16.3636 9.09091V3.63636L8.18182 0ZM6.36364 14.5455L2.72727 10.9091L4.00909 9.62727L6.36364 11.9727L12.3545 5.98182L13.6364 7.27273L6.36364 14.5455Z"
                fill="#FFC702"
              ></path>
            </svg>
          </div>
          {bio === true || username === true || editPass === true ? (
            <>
              {bio === true ? (
                <div className={styles.editBio}>
                  <label>Edit Bio</label>
                  <input
                    type="text"
                    value={userBio}
                    onChange={(e) => {
                      setUserBio(e.target.value);
                    }}
                  ></input>
                  <div className={styles.editsWrapper}>
                    <div
                      className={styles.saveBtn}
                      // onClick={() => editUsername(false)}
                      onClick={(e) => updateUserDetailHandler()}
                    >
                      Save Bio
                    </div>
                    <div
                      className={styles.cancelBtn}
                      onClick={() => editBio(false)}
                    >
                      Cancel
                    </div>
                  </div>
                </div>
              ) : null}
              {username === true ? (
                <div className={styles.editBio}>
                  <label>Edit Username</label>
                  <input
                    type="text"
                    value={userUsername}
                    onChange={(e) => {
                      setUserUsername(e.target.value);
                    }}
                  ></input>
                  <div className={styles.editsWrapper}>
                    <div
                      className={styles.saveBtn}
                      onClick={(e) => updateUserDetailHandler()}
                    >
                      Update Username
                    </div>
                    <div
                      className={styles.cancelBtn}
                      onClick={() => editUsername(false)}
                    >
                      Cancel
                    </div>
                  </div>
                </div>
              ) : null}
              {editPass === true ? (
                <div className={styles.editBio}>
                  <label>Current Password</label>
                  <input
                    type="text"
                    onChange={(e) => {
                      setUserPassword(e.target.value);
                    }}
                  ></input>
                  <label>New Password</label>
                  <input type="text"></input>
                  <div className={styles.editsWrapper}>
                    <div className={styles.saveBtn}>Change Password</div>
                    <div
                      className={styles.cancelBtn}
                      onClick={() => setEditPass(false)}
                    >
                      Cancel
                    </div>
                  </div>
                </div>
              ) : null}
            </>
          ) : (
            <>
              <div className={styles.editWrapper}>
                <div>
                  <p>Bio</p>
                  <h6>{userData?.bio}</h6>
                </div>
                <div className={styles.editBtn} onClick={() => editBio(true)}>
                  Edit Bio
                </div>
              </div>

              <div className={styles.editWrapper}>
                <div>
                  <p>Username</p>
                  <h6>{userData?.username}</h6>
                </div>
                <div
                  className={styles.editBtn}
                  onClick={() => editUsername(true)}
                >
                  Edit Username
                </div>
              </div>
              <div className={styles.editWrapper}>
                <div>
                  <p>Password</p>
                  <h6>*******</h6>
                </div>
                <div
                  className={styles.editBtn}
                  onClick={() => setEditPass(true)}
                >
                  Change
                </div>
              </div>
              <div className={styles.editWrapper}>
                <div>
                  <p>Joined Date</p>
                  <h6>{userData?.date_joined}</h6>
                </div>
                <div
                  className={styles.editBtn}
                  style={{ visibility: "hidden" }}
                >
                  Change
                </div>
              </div>
              <div className={styles.logoutBtn} onClick={logoutNavigator}>
                Logout
              </div>
            </>
          )}
        </div>
        <div className={styles.yourScripts}>
          <h4>Favourite</h4>
          <div className={styles.scriptsItems}>
            <div className="row">
              {favoriteC?.map((val, id) => {
                return (
                  <div
                    className="col-lg-3 ps-1 pe-1"
                    key={id}
                    onClick={() => specificScriptNavigator(val.content.id)}
                  >

                    <div
                      className={styles.items}
                      style={{
                        backgroundImage:
                          "url(" +
                          process.env.REACT_APP_Base_URL +
                          val.content.thumbnail +
                          ")",
                      }}
                    >
                      <div className={styles.itemsHeader}>
                        <div className={styles.itemsHeaderTop}>
                          <div className={styles.views}>
                            <svg
                              data-v-acc28e10=""
                              xmlns="http://www.w3.org/2000/svg"
                              fill="none"
                              viewBox="0 0 24 24"
                              stroke="currentColor"
                              className="h-4 w-4"
                            >
                              <path
                                data-v-acc28e10=""
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth="2"
                                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                              ></path>{" "}
                              <path
                                data-v-acc28e10=""
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth="2"
                                d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                              ></path>
                            </svg>
                            {val.content.views}
                          </div>
                          <div className={styles.uploadTime}>
                            {/*{moment(val.content.created_at).fromNow()}*/}
                          </div>
                        </div>
                        <div className={styles.itemsHeaderBottom}>
                          <div className={styles.free}>
                            <svg
                              data-v-acc28e10=""
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 20 20"
                              fill="currentColor"
                              className="h-5 w-5"
                            >
                              <path
                                data-v-acc28e10=""
                                fillRule="evenodd"
                                d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z"
                                clipRule="evenodd"
                              ></path>
                            </svg>
                            {val.content.type}
                          </div>
                        </div>
                      </div>
                      <div className={styles.itemsBottom}>
                        {/* <span>[UPDATE] 🔪Knife Strife!</span> */}
                        <div>
                          <div>
                            <h4>{val.content.title}</h4>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserProfile;
