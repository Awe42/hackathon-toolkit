import { useGetTablesQuery, useLazyGetTableDataQuery } from "../../features/tables/tablesApi"
import { Flex, Select, Table } from "@radix-ui/themes"


export const Tables = () => {
  const { data: tables, isSuccess: isTablesSuccess } = useGetTablesQuery()
  const [getTableData, { data: tableData, isSuccess: isTableDataSuccess }] = useLazyGetTableDataQuery()

  if (isTablesSuccess) {
    return (
      <Flex direction="column" justify="center" align="center" gap="5">
        <Select.Root onValueChange={(table: string) => {getTableData(table)}}>
          <Select.Trigger placeholder="Choose a table to display" />
          <Select.Content position="popper">
            <Select.Group>
              {tables.map((table: string) => (<Select.Item value={table} key={table}>{table}</Select.Item>))}
            </Select.Group>
          </Select.Content>
        </Select.Root>
        {isTableDataSuccess &&
        <Table.Root variant="surface">
          <Table.Header>
            <Table.Row>
              {Object.keys(tableData[0]).map((column: string) => (<Table.ColumnHeaderCell key={column}>{column}</Table.ColumnHeaderCell>))}
            </Table.Row>
          </Table.Header>

          <Table.Body>
            {tableData.map((row: Object, i: number) => (<Table.Row key={i}>
              {Object.values(row).map((rowItem: string) => (<Table.Cell key={rowItem}>{rowItem}</Table.Cell>))}
            </Table.Row>))}
          </Table.Body>
        </Table.Root>}
      </Flex>
    )
  }
}
