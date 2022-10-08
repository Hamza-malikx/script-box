// ** Third Party Components
import { useEffect, useState, useCallback } from "react";
import classnames from "classnames";
import { TrendingUp, User, Box, DollarSign } from "react-feather";
import axios from "axios";

// ** Custom Components
import Avatar from "@components/avatar";

// ** Reactstrap Imports
import {
  Card,
  CardHeader,
  CardTitle,
  CardBody,
  CardText,
  Row,
  Col,
} from "reactstrap";
import React from "react";

const StatsCard = ({ cols }) => {
  const [statsData, setStatsData] = useState([]);

  const getStats = useCallback(async () => {
    try {
      const api = `${process.env.REACT_APP_Base_URL}/api/adminPanel/get-statistics`;

      var res = await axios.get(api);
      if (res?.status === 200) {
        setStatsData(res?.data);
      }
    } catch (e) {
      console.log(e);
    }
  }, [setStatsData]);

  useEffect(() => {
    getStats();
  }, [getStats]);

  const data = [
    {
      title: statsData?.scripts,
      subtitle: "Scripts",
      color: "light-primary",
      icon: <TrendingUp size={24} />,
    },
    {
      title: statsData?.users,
      subtitle: "Users",
      color: "light-info",
      icon: <User size={24} />,
    },
    {
      title: statsData?.contents,
      subtitle: "Contents",
      color: "light-danger",
      icon: <Box size={24} />,
    },
    {
      title: statsData?.badges,
      subtitle: "Bagdes",
      color: "light-success",
      icon: <DollarSign size={24} />,
    },
  ];

  const renderData = () => {
    return data.map((item, index) => {
      const colMargin = Object.keys(cols);
      const margin = index === 2 ? "sm" : colMargin[0];
      return (
        <Col
          key={index}
          {...cols}
          className={classnames({
            [`mb-2 mb-${margin}-0`]: index !== data.length - 1,
          })}
        >
          <div className="d-flex align-items-center">
            <Avatar color={item.color} icon={item.icon} className="me-2" />
            <div className="my-auto">
              <h4 className="fw-bolder mb-0">{item.title}</h4>
              <CardText className="font-small-3 mb-0">{item.subtitle}</CardText>
            </div>
          </div>
        </Col>
      );
    });
  };

  return (
    <Card className="card-statistics">
      <CardHeader>
        <CardTitle tag="h4">Statistics</CardTitle>
        <CardText className="card-text font-small-2 me-25 mb-0">
          Updated an hour ago
        </CardText>
      </CardHeader>
      <CardBody className="statistics-body">
        <Row>{renderData()}</Row>
      </CardBody>
    </Card>
  );
};

export default StatsCard;
