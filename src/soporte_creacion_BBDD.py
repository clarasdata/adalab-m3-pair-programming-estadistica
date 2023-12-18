query_creacion_bbdd='''CREATE SCHEMA IF NOT EXISTS `pair_ETL` DEFAULT CHARACTER SET utf8 ;
'''

query_creacion_tabla_ventas='''
                                CREATE TABLE IF NOT EXISTS `pair_ETL`.`ventas` (
                                `id_venta` INT NOT NULL AUTO_INCREMENT,
                                `id_cliente` INT NOT NULL,
                                `id_producto` VARCHAR(45) NOT NULL,
                                `fecha_venta` VARCHAR(45) NOT NULL,
                                `cantidad` INT NOT NULL,
                                `total` FLOAT NOT NULL,
                                PRIMARY KEY (`id_venta`),
                                UNIQUE INDEX `id_venta_UNIQUE` (`id_venta` ASC) VISIBLE)
                                ENGINE = InnoDB;'''

query_insertar_ventas='INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad, total) VALUES (%s, %s, %s, %s, %s)'
