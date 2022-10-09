// ** Table Columns
import { data, userColumns } from "../data";

// ** Third Party Components
import { ChevronDown } from "react-feather";
import DataTable from "react-data-table-component";

// ** Reactstrap Imports
import { Card, CardHeader, CardTitle } from "reactstrap";
import React, {useState} from "react";
import {Col, Row} from "react-bootstrap";
import styles from "../../../pages/upload/upload.module.css";
import axios from "axios";
import {useHistory} from "react-router-dom";

const DataTablesBasic = () => {
    const [badge, setBadge] = useState([]);
    const [title, setTitle] = useState('');
    const [desc, setDesc] = useState('');
    const history = useHistory();


    const handleChangeInputFile = (e) => {
        setBadge(e.target.files[0]);
    };

    const submitHandler = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("image", badge);
        try {
            const config = {
                headers: {
                    "Content-Type": "application/json",
                },
            };

            const api = `${process.env.REACT_APP_Base_URL}/api/adminPanel/createBadge/`;

            var res = await axios.post(api, { 'title':title,'desc':desc });
            console.log(res);

            if (res.status === 200) {
                console.log(res);
                formData.append("id", res?.data?.id);
                const { data } = await axios.post(
                    `${process.env.REACT_APP_Base_URL}/api/adminPanel/imageUploadBadge/`,
                    formData
                );

                console.log(data);
                // history.push("../../data-tables/badgetable/");


            }
        } catch (e) {
            console.log(e);
        }
    };
    return (
    <Card className="overflow-hidden">
      <CardHeader>
        <CardTitle tag="h4">Badge Upload</CardTitle>
      </CardHeader>
      <div className="react-dataTable p-4">

          <Row >
              <Col sm="2"></Col>
              <Col sm='4'>
                  <input
                      className="form-control "
                      type="text"
                      placeholder="Title.."
                      name="Title"
                      // value={content.description}
                      onChange={(e) => setTitle(e.target.value)}
                  ></input>
              </Col>
              <Col sm="1"></Col>
              <Col sm='4'>
                  <input
                      className="form-control "
                      type="text"
                      placeholder="Description.."
                      name="description"
                      // value={content.description}
                      onChange={(e) => setDesc(e.target.value)}
                  ></input>
              </Col>
          </Row>
          <br/>
          <br/>
          <Row>
              <Col sm="2"></Col>
              <Col sm='4'>
                  <input
                      type="file"
                      name="image"
                      className="form-control"
                      onChange={handleChangeInputFile}
                  ></input>

              </Col> <Col sm="1"></Col>
              <Col sm='4'>
                  <button className="btn-sm btn-outline-light btn-primary" onClick={submitHandler}>
                      Add
                  </button>
              </Col>
          </Row>

      </div>
    </Card>
  );
};

export default DataTablesBasic;
