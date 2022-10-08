import React, { useEffect, useState } from "react";
import styles from "./styles.module.css";
import Header from "../home/navbar/Header";
import img from "../../../assets/images/avatars/xyz.jpg";
import avtr from "../../../assets/images/avatars/avatar.png";
import axios from "axios";

const SpecificScrip = ({ match }) => {
  const [content, setContent] = useState(null);
  const [favCheck, setFavCheck] = useState(false);
  const [loadSite, setLoadSite] = useState(false);
  const [comment, setComment] = useState("");
  const [comments, setComments] = useState([]);
  const [userDetails, setUserDetails] = useState(
    JSON.parse(localStorage.getItem("userData"))
  );
  const favClick = async (e) => {
    const { data } = await axios.post(
      `${process.env.REACT_APP_Base_URL}/api/user/addFavContent/`,
      { content: content.title, user: userDetails.username }
    );
    alert(data);
  };

  const postComment = async (e) => {
    const { data } = await axios.post(
      `${process.env.REACT_APP_Base_URL}/api/user/publishComment/`,
      { content: content.title, user: content.user, comment: comment }
    );
    if (data === "Commented Already") {
      alert(data);
    }
    setLoadSite(true);
  };

  const likeComment = async (id) => {
    console.log(id);
    const { data } = await axios.post(
        `${process.env.REACT_APP_Base_URL}/api/user/likeComment/`,
        {'id':id,
          'user':userDetails.username},
    );
    if (data === "Liked Already")
    {
      alert(data)
    }
    else {
      alert("Liked Comment")
    }
  };
  const dislikeComment = async (id) => {
    console.log(id);
    const { data } = await axios.post(
        `${process.env.REACT_APP_Base_URL}/api/user/disLikeComment/`,
        {'id':id,
          'user':userDetails.username},
    );
    if (data === "Disliked Already")
    {
      alert(data)
    }
    else {
      alert("Disliked Comment")
    }
  };

  const getContent = async () => {
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/user/content/${match.params.id}/`;

      var res = await axios.get(api);

      if (res.status === 200) {
        console.log(res.data);
        setContent(res.data);

        const { data } = await axios.post(
          `${process.env.REACT_APP_Base_URL}/api/user/checkFavContent/${res.data.title}/`,
        {  user: userDetails.username }

        );

        const { data: data2 } = await axios.get(
          `${process.env.REACT_APP_Base_URL}/api/user/getComment/${res.data.title}/`
        );

        setComments(data2);
        setFavCheck(data);
      }
      console.log(res);
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    getContent();
    setLoadSite(false);
  }, [loadSite,favCheck]);

  // useEffect(() => {
  //
  // }, [favCheck]);

  return (
    <div>
      <Header />
      <div className="container">
        <div>
          <div className={styles.hero}>
            <div className={styles.heroLeft}>
              <div className={styles.heroLeftRel}>
                <img
                  src={
                    content &&
                    process.env.REACT_APP_Base_URL + content.thumbnail
                  }
                  alt=""
                />
                <div className={styles.views}>
                  <div>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      className="h-4 w-4"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                      ></path>{" "}
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                      ></path>
                    </svg>{" "}
                    {content && content.views}
                  </div>
                </div>
                <div className={styles.free}>
                  <div>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      className="h-5 w-5"
                    >
                      <path
                        fillRule="evenodd"
                        d="M4 4a2 2 0 00-2 2v4a2 2 0 002 2V6h10a2 2 0 00-2-2H4zm2 6a2 2 0 012-2h8a2 2 0 012 2v4a2 2 0 01-2 2H8a2 2 0 01-2-2v-4zm6 4a2 2 0 100-4 2 2 0 000 4z"
                        clipRule="evenodd"
                      ></path>
                    </svg>{" "}
                    {content && content.type}
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.heroRight}>
              <div className={styles.heroRightUpper}>
                <h1
                  className="text-4xl flex items-center gap-x-3 font-500 color-dark dark:text-white"
                  style={{ overflowWrap: "anywhere" }}
                >
                  {content && content.title}
                </h1>
                <span className="font-500 color-dark dark:text-white">
                  Counter Blox: Remastered
                </span>
                <strong>
                  <span className="text-md">Uploaded by</span>
                  <a href="#">
                    <img src={avtr} alt="" />
                    {content && content.user}
                  </a>
                </strong>
                <div className="flex items-center gap-x-3">
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    className="block dark:hidden"
                  >
                    <path
                      fillRule="evenodd"
                      clipRule="evenodd"
                      d="M20 10C20 15.5228 15.5228 20 10 20C4.47715 20 0 15.5228 0 10C0 4.47715 4.47715 0 10 0C15.5228 0 20 4.47715 20 10ZM10 4C9.44771 4 9 4.44772 9 5V11C9 11.5523 9.44772 12 10 12H15C15.5523 12 16 11.5523 16 11C16 10.4477 15.5523 10 15 10H11V5C11 4.44772 10.5523 4 10 4Z"
                      fill="#16133E"
                    ></path>
                  </svg>{" "}
                  <svg
                    width="20"
                    height="20"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    className="hidden dark:block"
                  >
                    <path
                      fillRule="evenodd"
                      clipRule="evenodd"
                      d="M20 10C20 15.5228 15.5228 20 10 20C4.47715 20 0 15.5228 0 10C0 4.47715 4.47715 0 10 0C15.5228 0 20 4.47715 20 10ZM10 4C9.44771 4 9 4.44772 9 5V11C9 11.5523 9.44772 12 10 12H15C15.5523 12 16 11.5523 16 11C16 10.4477 15.5523 10 15 10H11V5C11 4.44772 10.5523 4 10 4Z"
                      fill="white"
                    ></path>
                  </svg>{" "}
                  <span className="dark:text-white text-md"> an hour ago</span>
                </div>
              </div>
              <div className={styles.heroRightLower}>
                <div className={styles.btnWrapper}>
                  <div className={styles.btnWrapperLeft}>
                    <a
                      href={content && content.link}
                      target="_blank"
                      rel="noreferrer"
                      className={styles.playGameBtn}
                    >
                      Play Game{" "}
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        className="h-6 w-6 flex-shrink-0"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
                        ></path>{" "}
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                        ></path>
                      </svg>
                    </a>
                    <button>
                      <svg
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                        className="w-6 h-6 dark:stroke-current dark:text-white"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
                        ></path>
                      </svg>{" "}
                      <span className="color-dark font-500 text-sm dark:text-white underline">
                        Copy Script
                      </span>
                    </button>
                  </div>
                  <div className={styles.btnWrapperRight}>
                    <a href="#">
                      <span> Direct Execute </span>{" "}
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        className="h-6 w-6"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                        ></path>
                      </svg>{" "}
                    </a>
                    <button>Set-up Direct Execute</button>
                  </div>
                </div>
                <div className={styles.iconsWrapper}>
                  <button>
                    <svg
                      width="22"
                      height="18"
                      viewBox="0 0 22 18"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      className={styles.likeIcon}
                    >
                      <path
                        fillRule="evenodd"
                        clipRule="evenodd"
                        d="M8.67387 1.36754C8.94944 0.55086 9.72309 0 10.5945 0H11.8895C13.0076 0 13.914 0.895431 13.914 2V6H19.362C20.867 6 21.8459 7.56463 21.1728 8.89443L17.1237 16.8944C16.7808 17.572 16.0798 18 15.3129 18H8.46599C7.69915 18 6.99813 17.572 6.65519 16.8944L5.09794 13.8177C4.85782 13.3433 4.8183 12.794 4.9881 12.2908L8.67387 1.36754Z"
                        fill="#9B9B9B"
                      ></path>{" "}
                      <path
                        fillRule="evenodd"
                        clipRule="evenodd"
                        d="M4.1114 6.05132C4.64177 6.22596 4.92841 6.79228 4.75161 7.31623L2.99226 12.5303C2.90736 12.7819 2.92712 13.0565 3.04718 13.2938L4.69669 16.5528C4.94671 17.0468 4.74403 17.6474 4.24399 17.8944C3.74395 18.1414 3.13591 17.9412 2.88589 17.4472L1.23638 14.1882C0.876187 13.4765 0.81692 12.6527 1.07161 11.8979L2.83097 6.68377C3.00776 6.15983 3.58103 5.87667 4.1114 6.05132Z"
                        fill="#9B9B9B"
                      ></path>
                    </svg>
                    <span className="font-400 dark:text-white text-sm">0</span>
                  </button>
                  <button>
                    <svg
                      width="22"
                      height="18"
                      viewBox="0 0 22 18"
                      fill="none"
                      xmlns="http://www.w3.org/2000/svg"
                      className="transform rotate-180"
                    >
                      <path
                        fillRule="evenodd"
                        clipRule="evenodd"
                        d="M8.67387 1.36754C8.94944 0.55086 9.72309 0 10.5945 0H11.8895C13.0076 0 13.914 0.895431 13.914 2V6H19.362C20.867 6 21.8459 7.56463 21.1728 8.89443L17.1237 16.8944C16.7808 17.572 16.0798 18 15.3129 18H8.46599C7.69915 18 6.99813 17.572 6.65519 16.8944L5.09794 13.8177C4.85782 13.3433 4.8183 12.794 4.9881 12.2908L8.67387 1.36754Z"
                        fill="#9B9B9B"
                      ></path>{" "}
                      <path
                        fillRule="evenodd"
                        clipRule="evenodd"
                        d="M4.1114 6.05132C4.64177 6.22596 4.92841 6.79228 4.75161 7.31623L2.99226 12.5303C2.90736 12.7819 2.92712 13.0565 3.04718 13.2938L4.69669 16.5528C4.94671 17.0468 4.74403 17.6474 4.24399 17.8944C3.74395 18.1414 3.13591 17.9412 2.88589 17.4472L1.23638 14.1882C0.876187 13.4765 0.81692 12.6527 1.07161 11.8979L2.83097 6.68377C3.00776 6.15983 3.58103 5.87667 4.1114 6.05132Z"
                        fill="#9B9B9B"
                      ></path>
                    </svg>
                    <span className="font-400 dark:text-white text-sm">0</span>{" "}
                  </button>
                  {console.log(favCheck)}
                  {!favCheck ? (
                    <button onClick={favClick}>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="#9B9B9B"
                        className={`h-6 w-6 ${styles.favoriteIcon}`}
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                        ></path>
                      </svg>
                      <span className="font-400 dark:text-white text-sm">
                        Favourite
                      </span>
                    </button>
                  ) : (
                    <button onClick={favClick}>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="#9B9B9B"
                        className={`h-6 w-6 ${styles.favoriteIcon} ${styles.fillSvg}`}
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                        ></path>
                      </svg>
                      <span className="font-400 dark:text-white text-sm">
                        Favourite
                      </span>
                    </button>
                  )}

                  <button>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      className={`h-6 w-6 ${styles.favoriteIcon}`}
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                      ></path>
                    </svg>
                    <span className="font-400 dark:text-white text-sm">
                      Report
                    </span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.description}>
        <h2 className="text-white font-500 text-3xl dark:text-white">
          Description
        </h2>
        <p>
          {content && content.description}
        </p>
      </div>

      {content &&
        content.script.map((val) => (
          <div className={styles.script}>
            <div className={styles.scriptHeader}>
              <h6 className="font-400 text-lg hover:underline dark:text-white">
                View Raw
              </h6>
            </div>
            <div className={styles.scriptGap}></div>
            <textarea
              disabled="disabled"
              name="script"
              placeholder="Write your script here..."
              cols="30"
              rows="10"
            >
              {val.script}
            </textarea>
          </div>
        ))}

      <div className={styles.comments}>
        <div className={styles.commentsHeader}>
          <div className={styles.commentsHeaderWrapper}>
            <span className="font-400 text-lg dark:text-white"> Comments </span>
            <div className="relative">
              <span className={styles.commentsCount}>{comments.length}</span>{" "}
              <svg
                width="35"
                height="30"
                viewBox="0 0 35 30"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M17.25 0C7.72207 0 0 6.23437 0 13.9286C0 17.25 1.44199 20.2902 3.84082 22.6808C2.99854 26.0558 0.181934 29.0625 0.148242 29.096C0 29.25 -0.0404297 29.4777 0.047168 29.6786C0.134766 29.8795 0.323437 30 0.539062 30C5.00654 30 8.35547 27.8705 10.0131 26.558C12.2165 27.3817 14.6625 27.8571 17.25 27.8571C26.7779 27.8571 34.5 21.6228 34.5 13.9286C34.5 6.23437 26.7779 0 17.25 0Z"
                  fill="#28AD6C"
                ></path>
              </svg>
            </div>
          </div>
        </div>
        <div className={styles.commentsRest}>
          {comments &&
            comments.map((val) => (
              <div className={styles.commentsMapper}>
                <div className={styles.commentsMapperLeft}>
                  <div className={styles.commentsMapperLeftProfileWrapper}>
                    <img src={avtr} alt="" />
                  </div>
                  <div
                    className={styles.commentsMapperLeftProfileContentWrapper}
                  >
                    <a href="#">{val.user}</a>
                    <p className="color-dark flex-grow text-base dark:text-white">
                      <span>{val.comment}</span>
                    </p>
                    <button className="color-gray text-xs dark:text-rblx-gray dark:hover:text-white">
                      Report
                    </button>
                  </div>
                </div>
                <div className={styles.commentsMapperRight}>
                  <span className="color-gray text-sm font-400 whitespace-nowrap dark:text-rblx-gray">
                    {val.created_at}
                  </span>
                  <div className="flex space-x-4 justify-end">
                    <button
                      id={val.id}
                      value={val.id}
                      type="button"
                      name="like"
                      onClick={(e) => likeComment(val.id)}
                      className="flex gap-2 items-center"
                    >
                      <svg
                        width="22"
                        height="18"
                        viewBox="0 0 22 18"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          fillRule="evenodd"
                          clipRule="evenodd"
                          d="M8.67387 1.36754C8.94944 0.55086 9.72309 0 10.5945 0H11.8895C13.0076 0 13.914 0.895431 13.914 2V6H19.362C20.867 6 21.8459 7.56463 21.1728 8.89443L17.1237 16.8944C16.7808 17.572 16.0798 18 15.3129 18H8.46599C7.69915 18 6.99813 17.572 6.65519 16.8944L5.09794 13.8177C4.85782 13.3433 4.8183 12.794 4.9881 12.2908L8.67387 1.36754Z"
                          fill="#9B9B9B"
                        ></path>{" "}
                        <path
                          fillRule="evenodd"
                          clipRule="evenodd"
                          d="M4.1114 6.05132C4.64177 6.22596 4.92841 6.79228 4.75161 7.31623L2.99226 12.5303C2.90736 12.7819 2.92712 13.0565 3.04718 13.2938L4.69669 16.5528C4.94671 17.0468 4.74403 17.6474 4.24399 17.8944C3.74395 18.1414 3.13591 17.9412 2.88589 17.4472L1.23638 14.1882C0.876187 13.4765 0.81692 12.6527 1.07161 11.8979L2.83097 6.68377C3.00776 6.15983 3.58103 5.87667 4.1114 6.05132Z"
                          fill="#9B9B9B"
                        ></path>
                      </svg>{" "}
                    </button>{" "}
                    <button
                      type="button"
                      name="dislike"
                      onClick={(e) => dislikeComment(val.id)}
                      className="flex gap-2 items-center"
                    >
                      <svg
                        width="22"
                        height="18"
                        viewBox="0 0 22 18"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                        className="transform rotate-180"
                      >
                        <path
                          fillRule="evenodd"
                          clipRule="evenodd"
                          d="M8.67387 1.36754C8.94944 0.55086 9.72309 0 10.5945 0H11.8895C13.0076 0 13.914 0.895431 13.914 2V6H19.362C20.867 6 21.8459 7.56463 21.1728 8.89443L17.1237 16.8944C16.7808 17.572 16.0798 18 15.3129 18H8.46599C7.69915 18 6.99813 17.572 6.65519 16.8944L5.09794 13.8177C4.85782 13.3433 4.8183 12.794 4.9881 12.2908L8.67387 1.36754Z"
                          fill="#9B9B9B"
                        ></path>{" "}
                        <path
                          fillRule="evenodd"
                          clipRule="evenodd"
                          d="M4.1114 6.05132C4.64177 6.22596 4.92841 6.79228 4.75161 7.31623L2.99226 12.5303C2.90736 12.7819 2.92712 13.0565 3.04718 13.2938L4.69669 16.5528C4.94671 17.0468 4.74403 17.6474 4.24399 17.8944C3.74395 18.1414 3.13591 17.9412 2.88589 17.4472L1.23638 14.1882C0.876187 13.4765 0.81692 12.6527 1.07161 11.8979L2.83097 6.68377C3.00776 6.15983 3.58103 5.87667 4.1114 6.05132Z"
                          fill="#9B9B9B"
                        ></path>
                      </svg>{" "}
                    </button>
                  </div>
                </div>
              </div>
            ))}

          <div className={styles.addCommentWrapper}>
            <div className={styles.commentsMapperLeftProfileWrapper}>
              <img src={avtr} alt="" />
            </div>
            <div className={styles.commentInp}>
              <textarea
                name="comment"
                placeholder="Comment your thoughts..."
                onChange={(e) => setComment(e.target.value)}
                rows="6"
              ></textarea>
            </div>
          </div>
          <div className={styles.postBtn} onClick={postComment}>
            Post
          </div>
        </div>
      </div>
      <div className={styles.tags}>
        <div className={styles.tagsHeader}>
          <h3 className="color-dark text-2xl font-500 dark:text-white">Tags</h3>{" "}
          <svg
            width="19"
            height="19"
            viewBox="0 0 19 19"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              clipRule="evenodd"
              d="M3.83215 0.719553C2.08577 0.652385 0.651896 2.08626 0.719065 3.83264L0.945339 9.71576C0.974385 10.471 1.2874 11.1874 1.8218 11.7218L7.99927 17.8993C9.17085 19.0708 11.0703 19.0708 12.2419 17.8993L17.8988 12.2424C19.0703 11.0708 19.0703 9.17133 17.8988 7.99976L11.7213 1.82229C11.1869 1.28789 10.4705 0.974873 9.71527 0.945827L3.83215 0.719553ZM8.24234 8.24234C9.02339 7.46129 9.02339 6.19496 8.24234 5.41391C7.46129 4.63286 6.19496 4.63286 5.41391 5.41391C4.63286 6.19496 4.63286 7.46129 5.41391 8.24234C6.19496 9.02339 7.46129 9.02339 8.24234 8.24234Z"
              fill="#16133E"
            ></path>
          </svg>
        </div>
        <div className={styles.tagsWrapper}>
          <div>Abc</div>
          <div>adsjkndsaa</div>
          <div>hjaskdas</div>
        </div>
      </div>
    </div>
  );
};

export default SpecificScrip;
