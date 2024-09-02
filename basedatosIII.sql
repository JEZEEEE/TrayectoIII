CREATE TABLE usuario (
    cod_usu SERIAL PRIMARY KEY, -- Clave primaria de la tabla usuario
    cor_usu VARCHAR(50) UNIQUE NOT NULL, -- Correo del usuario
    con_usu VARCHAR(50) NOT NULL, -- Contraseña del usuario
    fky_per INTEGER REFERENCES personas(cod_per) , -- Clave foránea que referencia a la tabla personas
    fky_rol INTEGER REFERENCES rol(cod_rol), -- Clave foránea que referencia a la tabla roles
    est_usu char(1) NOT NULL -- Estado del usuario
);

-- Tabla de roles
CREATE TABLE rol (
    cod_rol SERIAL PRIMARY KEY, -- Clave primaria de la tabla rol
    nom_rol VARCHAR(50), -- Nombre del rol
    est_rol char(1) NOT NULL -- Estado del rol
);

-- Tabla de permisos
CREATE TABLE permisos (
    cod_perm SERIAL PRIMARY KEY, -- Clave primaria de la tabla permisos
    nom_perm VARCHAR(50), -- Nombre del permiso
    des_perm VARCHAR(220), -- Descripción del permiso
    est_perm char(1) NOT NULL -- Estado del permiso
);


-- Tabla de usuarios_permisos
CREATE TABLE usuario_permisos (
    cod_usu_perm SERIAL PRIMARY KEY, --- Clave primaria tabla usuario permisos
    fky_usu INTEGER REFERENCES usuario(cod_usu), -- Clave foránea que referencia a la tabla usuario
    fky_perm INTEGER REFERENCES permisos(cod_perm), -- Clave foránea que referencia a la tabla permisos
    PRIMARY KEY (fky_usu, fky_perm), -- Clave primaria de la tabla usuario_permisos
    est_usu_perm char(1) NOT NULL
);


CREATE TABLE personas (
    cod_per SERIAL PRIMARY KEY, -- Clave primaria de la tabla personas
    nom_per VARCHAR(50), -- Nombre de la persona
    ape_per VARCHAR(50), -- Apellido de la persona
    cor_per VARCHAR(50) UNIQUE, -- Correo de la persona
    fky_rol INTEGER REFERENCES rol(cod_rol), -- Clave foránea que referencia a la tabla rol
    est_per char(1) NOT NULL -- Estado de la persona
);

-- Tabla de tipos de personas
CREATE TABLE tipo_persona (
    cod_tip_per SERIAL PRIMARY KEY, -- Clave primaria de la tabla tipo_persona
    nom_tip_per VARCHAR(50), -- Nombre del tipo de persona
    est_tip_per char(1) NOT NULL -- Estado del tipo de persona
);


CREATE TABLE producto (
    cod_prod SERIAL PRIMARY KEY, -- Clave primaria de la tabla producto
    nom_prod VARCHAR(50), -- Nombre del producto
    pre_prod NUMERIC(10, 2), -- Precio del producto
    fky_cat INTEGER REFERENCES categoria(cod_cat), -- Clave foránea que referencia a la tabla categoría
    fky_mar INTEGER REFERENCES marca(cod_mar), -- Clave foránea que referencia a la tabla marca
    est_prod char(1) NOT NULL-- Estado del producto
);

-- Tabla de categorías
CREATE TABLE categoria (
    cod_cat SERIAL PRIMARY KEY, -- Clave primaria de la tabla categoría
    nom_cat VARCHAR(50), -- Nombre de la categoría
    est_cat char(1) NOT NULL-- Estado de la categoría
);

-- Tabla de marcas
CREATE TABLE marca (
    cod_mar SERIAL PRIMARY KEY, -- Clave primaria de la tabla marca
    nom_mar VARCHAR(50), -- Nombre de la marca
    est_mar char(1) NOT NULL -- Estado de la marca
);

-- Tabla intermedia para relacionar productos con categorías
CREATE TABLE producto_categoria (
    cod_prod_cat SERIAL PRIMARY KEY, -- Clave primaria 
    fky_prod INTEGER REFERENCES producto(cod_prod), -- Clave foránea que referencia a la tabla producto
    fky_cat INTEGER REFERENCES categoria(cod_cat), -- Clave foránea que referencia a la tabla categoría
    PRIMARY KEY (fky_prod, fky_cat), -- Clave primaria de la tabla producto_categoria
    est_prod_cat char(1) NOT NULL -- Estado de la relación producto-categoría
);

-- Tabla intermedia para relacionar productos con marcas
CREATE TABLE producto_marca (
    cod_prod_mar SERIAL PRIMARY KEY, -- Clave primaria 
    fky_prod INTEGER REFERENCES producto(cod_prod), -- Clave foránea que referencia a la tabla producto
    fky_mar INTEGER REFERENCES marca(cod_mar), -- Clave foránea que referencia a la tabla marca
    PRIMARY KEY (fky_prod, fky_mar), -- Clave primaria de la tabla producto_marca
    est_prod_mar char(1) NOT NULL -- Estado de la relación producto-marca
);

CREATE TABLE venta (
    cod_ven SERIAL PRIMARY KEY, -- Clave primaria de la tabla venta
    fec_ven DATE, -- Fecha de la venta
    fky_prod INTEGER REFERENCES producto(cod_prod), -- Clave foránea que referencia a la tabla producto
    fky_tip_pag INTEGER REFERENCES tipo_pago(cod_tip_pag), -- Clave foránea que referencia a la tabla tipo_pago
    fky_mon INTEGER REFERENCES moneda(cod_mon), -- Clave foránea que referencia a la tabla moneda
    est_ven char(1) NOT NULL -- Estado de la venta
);

-- Tabla de tipos de pago
CREATE TABLE tipo_pago (
    cod_tip_pag SERIAL PRIMARY KEY, -- Clave primaria de la tabla tipo_pago
    nom_tip_pag VARCHAR(50), -- Nombre del tipo de pago
    est_tip_pag char(1) NOT NULL -- Estado del tipo de pago
);

-- Tabla de monedas
CREATE TABLE moneda (
    cod_mon SERIAL PRIMARY KEY, -- Clave primaria de la tabla moneda
    nom_mon VARCHAR(50), -- Nombre de la moneda
    est_mon char(1) NOT NULL -- Estado de la moneda
);

-- Tabla intermedia para relacionar ventas con productos
CREATE TABLE venta_producto (
    fky_ven INTEGER REFERENCES venta(cod_ven), -- Clave foránea que referencia a la tabla venta
    fky_prod INTEGER REFERENCES producto(cod_prod), -- Clave foránea que referencia a la tabla producto
    PRIMARY KEY (fky_ven, fky_prod), -- Clave primaria de la tabla venta_producto
    est_ven_prod char(1) NOT NULL -- Estado de la relación venta-producto
);


CREATE TABLE cliente (
    cod_cli SERIAL PRIMARY KEY, -- Clave primaria de la tabla cliente
    nom_cli VARCHAR(50), -- Nombre del cliente
    ape_cli VARCHAR(50), -- Apellido del cliente
    cor_cli VARCHAR(50), -- Correo del cliente
    con_cli VARCHAR(50), -- Contraseña del cliente
    fky_per INTEGER REFERENCES personas(cod_per), -- Clave foránea que referencia a la tabla personas
    est_cli char(1)  NOT NULL-- Estado del cliente
);

-- Tabla de proveedores
CREATE TABLE proveedor (
    cod_prov SERIAL PRIMARY KEY, -- Clave primaria de la tabla proveedor
    nom_prov VARCHAR(50), -- Nombre del proveedor
    ape_prov VARCHAR(50), -- Apellido del proveedor
    cor_prov VARCHAR(50), -- Correo del proveedor
    con_prov VARCHAR(50), -- Contraseña del proveedor
    fky_per INTEGER REFERENCES personas(cod_per), -- Clave foránea que referencia a la tabla personas
    est_prov char(1) NOT NULL -- Estado del proveedor
);

-- Tabla de órdenes
CREATE TABLE ordenes.ordenes (
    cod_ord SERIAL PRIMARY KEY, -- Clave primaria de la tabla órdenes
    fec_ord DATE, -- Fecha de la orden
    fky_cli INTEGER REFERENCES cliente(cod_cli), -- Clave foránea que referencia a la tabla cliente
    fky_prov INTEGER REFERENCES proveedor(cod_prov), -- Clave foránea que referencia a la tabla proveedor
    est_ord char(1)  NOT NULL-- Estado de la orden
);

-- Tabla intermedia para relacionar órdenes con clientes y proveedores
CREATE TABLE orden_cliente_proveedor (
    fky_ord INTEGER REFERENCES ordenes(cod_ord), -- Clave foránea que referencia a la tabla órdenes
    fky_cli INTEGER REFERENCES cliente(cod_cli), -- Clave foránea que referencia a la tabla cliente
    fky_prov INTEGER REFERENCES proveedor(cod_prov), -- Clave foránea que referencia a la tabla proveedor
    PRIMARY KEY (fky_ord, fky_cli, fky_prov), -- Clave primaria de la tabla orden_cliente_proveedor
    est_ord_cli char(1) NOT NULL -- Estado de la relación orden-cliente-proveedor
);