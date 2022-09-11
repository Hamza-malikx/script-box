import React, { useState, useEffect } from "react";
import styles from "./home.module.css";
import Header from "./navbar/Header";
import Switch from "react-switch";
import { Link } from "react-router-dom";
import axios from "axios";
import moment from "moment";

const Home = () => {
  const [content, setContent] = useState(null);
  const [switchState, setSwitchState] = useState(false);
  console.log();
  const handleChange = (nextChecked) => {
    setSwitchState(nextChecked);
  };
  const getContent = async () => {
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/user/allContent/`;

      var res = await axios.get(api);
      if (res.status === 200) {
        setContent(res.data);
      }
      console.log(res);
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    getContent();
  }, []);
  return (
    <div>
      <Header />
      <div className={`${styles.hero}`}>
        <div className="container">
          <div className={`${styles.heroInner}`}>
            <h1>
              <span>Script</span>Blox
            </h1>
            <p>
              Search the best lua scripts available in the community uploaded by
              users!
            </p>
            <div className={styles.searchWrapper}>
              <input
                autoComplete="off"
                type="search"
                placeholder='Try "bloxburg"'
                className="bg-white rounded-md w-full focus:outline-none"
              ></input>
              <div className={styles.switchWrapper}>
                <Switch
                  className={`reactSwitch`}
                  onChange={handleChange}
                  checked={switchState}
                  height={25}
                  uncheckedIcon={
                    <div
                      style={{
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        height: "100%",
                        fontSize: 11,
                        color: "white",
                        paddingRight: 2,
                      }}
                    >
                      Free
                    </div>
                  }
                  checkedIcon={
                    <div
                      style={{
                        display: "flex",
                        justifyContent: "center",
                        alignItems: "center",
                        height: "100%",
                        fontSize: 11,
                        color: "white",
                        // paddingRight: 2,
                        paddingLeft: 2,
                      }}
                    >
                      Paid
                    </div>
                  }
                />
                <button className={styles.searchBtn}>Search</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.recentScripts}>
        <div className="container-fluid">
          <div className={styles.recentScriptsInner}>
            <div className={styles.recentScriptsHeader}>
              <div className={styles.recentScriptsHeaderLeft}>
                <h3>Recent Scripts</h3>
                <button className={styles.filterBtn}>
                  <svg
                    fill="none"
                    stroke="#fff"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                    className="w-6 h-6"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                    ></path>
                  </svg>
                </button>
              </div>
              <div className={styles.recentScriptsHeaderRight}>
                <Link to="/upload" className={styles.uploadBtn}>
                  <span>Upload</span>
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fillRule="evenodd"
                      clipRule="evenodd"
                      d="M20 10C20 15.5228 15.5228 20 10 20C4.47715 20 0 15.5228 0 10C0 4.47715 4.47715 0 10 0C15.5228 0 20 4.47715 20 10ZM9 6C9 5.44772 9.44772 5 10 5C10.5523 5 11 5.44772 11 6V9H14C14.5523 9 15 9.44772 15 10C15 10.5523 14.5523 11 14 11H11V14C11 14.5523 10.5523 15 10 15C9.44772 15 9 14.5523 9 14V11H6C5.44772 11 5 10.5523 5 10C5 9.44772 5.44772 9 6 9H9V6Z"
                      fill="#FBFBFF"
                    ></path>
                  </svg>
                </Link>
              </div>
            </div>
            <div className={styles.scriptsItems}>
              <div className="row">
                {content?.map((val, id) => {
                  return (
                    <div className="col-lg-3 ps-1 pe-1" key={id}>
                      <div
                        className={styles.items}
                        style={{
                          backgroundImage:
                            "url(" +
                            process.env.REACT_APP_Base_URL +
                            val.thumbnail +
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
                              {val.views}
                            </div>
                            <div className={styles.uploadTime}>
                              {moment(val.created_at).fromNow()}
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
                              {val.type}
                            </div>
                          </div>
                        </div>
                        <div className={styles.itemsBottom}>
                          {/* <span>[UPDATE] 🔪Knife Strife!</span> */}
                          <div>
                            <div>
                              <h4>{val.title}</h4>
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
    </div>
  );
};

export default Home;
