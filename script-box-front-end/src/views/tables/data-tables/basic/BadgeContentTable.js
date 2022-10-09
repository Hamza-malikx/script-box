// ** Table Columns
import { BadgeContentData, badgeContentColumns } from "../data";

// ** Third Party Components
import { ChevronDown } from "react-feather";
import DataTable from "react-data-table-component";

// ** Reactstrap Imports
import { Card, CardHeader, CardTitle } from "reactstrap";

const DataTablesBasic = () => {
  return (
    <Card className="overflow-hidden">
      <CardHeader>
        <CardTitle tag="h4">Badge Content Criteria </CardTitle>
      </CardHeader>
      <div className="react-dataTable">
        <DataTable
          noHeader
          pagination
          data={BadgeContentData}
          columns={badgeContentColumns}
          className="react-dataTable"
          sortIcon={<ChevronDown size={10} />}
          paginationRowsPerPageOptions={[10, 25, 50, 100]}
        />
      </div>
    </Card>
  );
};

export default DataTablesBasic;
