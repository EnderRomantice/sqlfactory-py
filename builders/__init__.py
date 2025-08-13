class SQLBuilder:
    @staticmethod
    def build_insert(table, data):
        """构建INSERT语句
        Args:
            table: 表名
            data: 要插入的数据字典
        Returns:
            tuple: (SQL语句, 参数列表)
        """
        fields = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO {table} ({fields}) VALUES ({placeholders})"
        params = list(data.values())
        return sql, params

    @staticmethod
    def build_update(table, data, where):
        """构建UPDATE语句
        Args:
            table: 表名
            data: 要更新的数据字典
            where: WHERE条件字典
        Returns:
            tuple: (SQL语句, 参数列表)
        """
        set_clause = ', '.join([f"{k} = %s" for k in data.keys()])
        where_clause = ' AND '.join([f"{k} = %s" for k in where.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        params = list(data.values()) + list(where.values())
        return sql, params

    @staticmethod
    def build_delete(table, where):
        """构建DELETE语句
        Args:
            table: 表名
            where: WHERE条件字典
        Returns:
            tuple: (SQL语句, 参数列表)
        """
        where_clause = ' AND '.join([f"{k} = %s" for k in where.keys()])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        params = list(where.values())
        return sql, params