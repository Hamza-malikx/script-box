import React, { useState, useEffect } from "react";
import styles from "./upload.module.css";
import Header from "../home/navbar/Header";
import Switch from "react-switch";
import axios from "axios";
const Upload = () => {
  const [thumbnail, setThumbnail] = useState([]);
  const [content, setContent] = useState({
    user: "hamza2",
    title: "",
    link: "",
    is_varfied: false,
    is_universal: false,
    description: "",
    features: "",
    tag: "",
    type: "free",
    privacy: "",
    script: "",
    // image: null,
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
  console.log(content);

  const handleChangeInput = (e) => {
    setContent({ ...content, [e.target.name]: e.target.value });
    console.log(content);
  };
  const handleChangeInputFile = (e) => {
    setThumbnail(e.target.files[0]);
  };
  console.log(thumbnail);

  const submitHandler = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("image", thumbnail);
    for (var key of formData.entries()) {
      console.log(key[0] + ", " + key[1]);
    }
    console.log({ ...content, image: formData });
    try {
      // console.log(content);
      const config = {
        headers: {
          "Content-Type": "application/json",
        },
      };
      const api = `${process.env.REACT_APP_Base_URL}/user/uploadContent/`;
      var res = await axios.post(api, { ...content, image: formData }, config);
      console.log(content);
      if (res.status === 200) {
        // setContent(res.data);
      }
      console.log(res);
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    // submitHandler();
  }, []);
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
          <label>Upload Custom Thumbnail (optional)</label>
          <br />
          <p>NOTE: Recommended image aspect ratio should be 16:9</p>
          <input
            type="file"
            name="image"
            // value={content.image}
            onChange={handleChangeInputFile}
          ></input>
          <label>Features*</label>
          <br />
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
          <textArea
            className="form-control"
            type="text"
            placeholder="Describe script features"
            name="features"
            value={content.features}
            onChange={handleChangeInput}
          ></textArea>
          <label>Add tags</label>
          <br />
          <input
            className="form-control"
            type="text"
            placeholder="Enter Tags (Separate with comma/enter)"
            name="tag"
            value={content.tag}
            onChange={handleChangeInput}
          ></input>
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
          <label>Paste Your script</label>
          <br />
          <input
            className="form-control"
            type="text"
            placeholder="Write your script here..."
            name="script"
            value={content.script}
            onChange={handleChangeInput}
          ></input>
          <p>Privacy:</p>
          <div className={styles.radioBtns}>
            <input
              type="radio"
              id="age1"
              name="privacy"
              value="Public"
              onChange={handleChangeInput}
            />
            <input
              type="radio"
              id="age2"
              name="privacy"
              value="Unlisted"
              onChange={handleChangeInput}
            />
            <input
              type="radio"
              id="age3"
              name="privacy"
              value="Private"
              onChange={handleChangeInput}
            />
            <br />
          </div>
          <button className="btn btn-primary" onClick={submitHandler}>
            Upload
          </button>
        </form>
      </div>
    </div>
  );
};

export default Upload;
