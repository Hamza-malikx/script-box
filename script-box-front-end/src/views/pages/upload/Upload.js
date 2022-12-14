import React, { useState } from "react";
import styles from "./upload.module.css";
import Header from "../home/navbar/Header";
import Switch from "react-switch";
import axios from "axios";
const Upload = () => {
  const [thumbnail, setThumbnail] = useState([]);
  const [content, setContent] = useState({
    user: "hamza",
    title: "",
    link: "",
    is_varfied: false,
    is_universal: false,
    description: "",
    features: "",
    tag: "",
    type: "free",
    privacy: "",
    script: [],
    // image: "",
  });
  const [switchState, setSwitchState] = useState(false);
  const [switchVerState, setSwitchVerState] = useState(false);
  const [type, setTypeState] = useState(false);

  const handleUniScriptChange = (nextChecked) => {
    setSwitchState(nextChecked);
    setContent({ ...content, is_universal: nextChecked });
  };
  const handleVerifiedScriptChange = (nextChecked) => {
    setSwitchVerState(nextChecked);
    setContent({ ...content, is_varfied: nextChecked });
  };
  const handleTypeChange = (nextChecked) => {
    setTypeState(nextChecked);
    setContent({ ...content, type: nextChecked ? "paid" : "free" });
  };

  const handleChangeInput = (e) => {
    setContent({ ...content, [e.target.name]: e.target.value });
  };
  const handleChangeInputFile = (e) => {
    setThumbnail(e.target.files[0]);
  };

  // Add multiple input
  const inputArr = [
    {
      type: "text",
      id: 1,
      value: "",
    },
  ];

  const [arr, setArr] = useState(inputArr);

  const addInput = (e) => {
    e.preventDefault();
    setArr((s) => {
      return [
        ...s,
        {
          type: "text",
          value: "",
        },
      ];
    });
  };
  const handleChange = (e) => {
    e.preventDefault();
    const index = e.target.id;
    setArr((s) => {
      const newArr = s.slice();
      newArr[index].value = e.target.value;

      return newArr;
    });
  };
  console.log(arr);
  const submitHandler = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    setContent({ ...content, script: arr });
    formData.append("image", thumbnail);
    try {
      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };

      const api = `${process.env.REACT_APP_Base_URL}/api/user/uploadContent/`;

      var res = await axios.post(api, { ...content, image: formData }, config);
      console.log(res);
      console.log(content);
      console.log(formData);
      if (res.status === 200) {
        console.log(res);
        formData.append("id", res?.data?.id);
        const { data } = await axios.post(
          `${process.env.REACT_APP_Base_URL}/api/user/uploadContentImage/`,
          formData,
          config
        );

        // const formData = new FormData();
        // formData.append("scripts", arr);
        // const appData = {
        //   scripts: arr,
        // };
        // const resData = await axios.post(
        //   `${process.env.REACT_APP_Base_URL}/api/user/uploadMultipleScripts/`,
        //   appData,
        //   config
        // );

        // console.log(resData);
      }
    } catch (e) {
      console.log(e);
    }
  };
  console.log(content);
  return (
    <div>
      <Header />
      <div className={styles.upload}>
        <form>
          <h2>Upload Script</h2>
          <label>
            Title of the Script* (Do not include game name in title!)
          </label>
          <br />
          <input
            className="form-control"
            type="text"
            placeholder="Enter title Of the script"
            name="title"
            value={content.title}
            onChange={handleChangeInput}
          ></input>
          <div className={styles.universalScriptWrapper}>
            <label>Is Universal Script?*</label>
            <Switch
              className={`reactSwitch`}
              onChange={handleUniScriptChange}
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
                  No
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
                  Yes
                </div>
              }
            />
          </div>
          <div className={styles.gameLink}>
            <label>Game link*</label>
            <br />
            <input
              className="form-control"
              type="text"
              placeholder="Enter link of the game (Eg. www.roblox.com/games/game-id)"
              name="link"
              value={content.link}
              onChange={handleChangeInput}
            ></input>
          </div>
          <label>Upload Custom Thumbnail (optional)</label>
          <br />
          <p>NOTE: Recommended image aspect ratio should be 16:9</p>
          <div className={styles.fileInp}>
            <input
              type="file"
              name="image"
              className="form-control"
              onChange={handleChangeInputFile}
            ></input>
          </div>
          <div className={styles.verifiedS}>
            <label>Verified Script</label>
            <br />

            <Switch
              className={`reactSwitch`}
              onChange={handleVerifiedScriptChange}
              checked={switchVerState}
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
                  No
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
                  Yes
                </div>
              }
            />
          </div>
          <div className={styles.textAreaWrapper}>
            <textarea
              className="form-control"
              type="text"
              placeholder="Describe script features"
              name="features"
              value={content.features}
              onChange={handleChangeInput}
            ></textarea>
          </div>
          <div className={styles.addTagsWrapper}>
            <label>Add tags (separate tags with commas)</label>
            <br />
            <input
              className="form-control"
              type="text"
              placeholder="Enter Tags (Separate with comma/enter)"
              name="tag"
              value={content.tag}
              onChange={handleChangeInput}
            ></input>
          </div>
          <label>Description</label>
          <br />

          <input
            className="form-control"
            type="text"
            placeholder="Description..."
            name="description"
            value={content.description}
            onChange={handleChangeInput}
          ></input>
          <div className={styles.typeWrapper}>
            <label>Type</label>
            <br />

            <Switch
              className={`reactSwitch`}
              onChange={handleTypeChange}
              checked={type}
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
                  free
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
                  paid
                </div>
              }
            />
          </div>
          <br />
          <div className={styles.pasteScriptWrapper}>
            <label>Paste Your script</label>
            <br />
            {arr.map((item, i) => {
              return (
                <textarea
                  key={i}
                  onChange={handleChange}
                  value={item.value}
                  id={i}
                  type={item.type}
                  // size="40"
                  name="script"
                  className="form-control"
                  placeholder="Write your script here..."
                />
              );
            })}
            {/* <textarea
              className="form-control"
              type="text"
              placeholder="Write your script here..."
              name="script"
              value={content.script}
              onChange={handleChangeInput}
            ></textarea> */}
            <button className={styles.addScriptBtn} onClick={addInput}>
              Add
            </button>
          </div>
          <p className={styles.privacy}>Privacy:</p>
          <div className={styles.radioBtns}>
            <label>
              <input
                type="radio"
                id="age1"
                name="privacy"
                value="Public"
                onChange={handleChangeInput}
              />
              <span>Public ????</span>
            </label>
            <label>
              <input
                type="radio"
                id="age2"
                name="privacy"
                value="Unlisted"
                onChange={handleChangeInput}
              />
              <span>Unlisted ????</span>
            </label>
            <label>
              <input
                type="radio"
                id="age3"
                name="privacy"
                value="Private"
                onChange={handleChangeInput}
              />
              <span>Private ????</span>
            </label>

            <br />
          </div>
          <button
            className={`btn btn-primary ${styles.uploadBtn}`}
            onClick={submitHandler}
          >
            Upload
          </button>
        </form>
      </div>
    </div>
  );
};

export default Upload;
