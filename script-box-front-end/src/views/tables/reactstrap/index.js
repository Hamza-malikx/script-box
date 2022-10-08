// ** React Imports
import { Fragment } from "react";

// ** Third Party Components
import { Row, Col } from "reactstrap";
import ContentsListTable from "../data-tables/basic/ContentsListTable";
import "@styles/react/libs/tables/react-dataTable-component.scss";

const Tables = () => {
  return (
    <Fragment>
      <Row>
        <Col sm="12">
          <ContentsListTable />
        </Col>
      </Row>
    </Fragment>
  );
};

export default Tables;
