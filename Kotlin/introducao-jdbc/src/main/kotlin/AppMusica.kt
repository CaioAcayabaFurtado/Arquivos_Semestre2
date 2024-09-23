import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.JdbcTemplate

fun main() {
    val datasource = BasicDataSource()
    datasource.driverClassName = "org.h2.driver"
//    caso queira salvar em um arquivo, como se fosse em um BD
//    datasource.url = "jdbc:h2:file:./festival"
    datasource.url = "jdbc:h2:mem:festival"
    datasource.username= "sa"
    datasource.password= ""
    
    val jdbcTemplate = JdbcTemplate(datasource)
}
