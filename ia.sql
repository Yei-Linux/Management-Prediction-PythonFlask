-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-09-2019 a las 07:59:40
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidato`
--

CREATE TABLE `candidato` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `ID_UNIVERSIDAD` int(11) NOT NULL,
  `EDAD` varchar(20) NOT NULL,
  `ANTECEDENTES_CORRUPCION` varchar(10) NOT NULL,
  `GRADO_ESTUDIO` varchar(10) NOT NULL,
  `ESTUDIOS_GESTION_PUBLICA` varchar(10) NOT NULL,
  `PROFESION` varchar(15) NOT NULL,
  `PRODUCCION_CIENTIFICA` varchar(10) NOT NULL,
  `PROYECTOS_INVESTIGACION` varchar(10) NOT NULL,
  `EXPERIENCIA` varchar(10) NOT NULL,
  `ANOS_EXPERIENCIA` varchar(30) NOT NULL,
  `GENERO` varchar(10) NOT NULL,
  `TIPO_PERSONALIDAD` varchar(30) NOT NULL,
  `EX_RECTOR` varchar(10) NOT NULL,
  `FILENAME` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `candidato`
--

INSERT INTO `candidato` (`ID`, `NOMBRE`, `ID_UNIVERSIDAD`, `EDAD`, `ANTECEDENTES_CORRUPCION`, `GRADO_ESTUDIO`, `ESTUDIOS_GESTION_PUBLICA`, `PROFESION`, `PRODUCCION_CIENTIFICA`, `PROYECTOS_INVESTIGACION`, `EXPERIENCIA`, `ANOS_EXPERIENCIA`, `GENERO`, `TIPO_PERSONALIDAD`, `EX_RECTOR`, `FILENAME`) VALUES
(2, 'JUAN NUNURA CHULLY', 1, 'Adulto Mayor', 'No', 'Doctorado', 'No', 'Economista', 'Si', 'Si', 'Si', '11-15', 'M', 'COMANDANTE', 'Si', '2.png'),
(3, 'PABLO ARELLANO UBILLUZ', 1, 'Adulto', 'Si', 'Doctorado', 'Si', 'Ingeniero', 'No', 'Si', 'Si', '11-15', 'M', 'ANIMADOR', 'No', '3.png'),
(4, 'JOSE TEZEN CAMPOS', 1, 'Adulto', 'No', 'Doctorado', 'No', 'Ingeniero', 'No', 'Si', 'Si', '16 a mas', 'M', 'EMPRENDEDOR', 'No', '4.png'),
(5, 'BALDO OLIVARES CHOQUE', 1, 'Adulto', 'No', 'Doctorado', 'Si', 'Ingeniero', 'No', 'Si', 'Si', '11-15', 'M', 'INNOVADOR', 'Si', '5.png'),
(6, 'ANÍBAL EDUARDO ISMODES CASCÓN', 2, 'Adulto Mayor', 'No', 'Doctorado', 'No', 'Ingeniero', 'Si', 'Si', 'Si', '16 a mas', 'M', 'LOGICO', 'Si', '6.png'),
(7, 'JORGE MARCIAL BLONDET SAAVEDRA', 2, 'Adulto', 'No', 'Doctorado', 'Si', 'Ingeniero', 'No', 'Si', 'Si', '16 a mas', 'M', 'LOGICO', 'No', '7.png'),
(8, 'EFRAIN GONZALES DE OLARTE', 2, 'Adulto', 'No', 'Doctorado', 'No', 'Economista', 'No', 'Si', 'Si', '16 a mas', 'M', 'ARQUITECTO', 'No', '8.png'),
(9, 'CARLOS FOSCA PASTOR', 2, 'Adulto Mayor', 'No', 'Doctorado', 'No', 'Docente', 'Si', 'Si', 'Si', '11-15', 'M', 'INNOVADOR', 'Si', '9.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rectores`
--

CREATE TABLE `rectores` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `UNIVERSIDAD` varchar(50) NOT NULL,
  `ANTECEDENTES_CORRUPCION` varchar(10) NOT NULL,
  `ESTUDIOS_GESTION_PUBLICA` varchar(10) NOT NULL,
  `PROFESION` varchar(15) NOT NULL,
  `PRODUCCION_CIENTIFICA` varchar(10) NOT NULL,
  `PROYECTOS_INVESTIGACION` varchar(10) NOT NULL,
  `EXPERIENCIA` varchar(10) NOT NULL,
  `ANOS_EXPERIENCIA` varchar(30) NOT NULL,
  `GENERO` varchar(10) NOT NULL,
  `EX_RECTOR` varchar(10) NOT NULL,
  `TIPO_PERSONALIDAD` varchar(30) NOT NULL,
  `GESTION` varchar(10) NOT NULL,
  `TIPO_UNIV` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `rectores`
--

INSERT INTO `rectores` (`ID`, `NOMBRE`, `UNIVERSIDAD`, `ANTECEDENTES_CORRUPCION`, `ESTUDIOS_GESTION_PUBLICA`, `PROFESION`, `PRODUCCION_CIENTIFICA`, `PROYECTOS_INVESTIGACION`, `EXPERIENCIA`, `ANOS_EXPERIENCIA`, `GENERO`, `EX_RECTOR`, `TIPO_PERSONALIDAD`, `GESTION`, `TIPO_UNIV`) VALUES
(1, 'Marcial Rubio Correa', 'PUCP', 'No', 'No', 'Abogado', 'Si', 'Si', 'Si', '11-15', 'M', 'Si', 'ARQUITECTO', '10', 'Privada'),
(2, 'Baldo Andrés Olivares Choque', 'UNAC', 'No', 'Si', 'Ingeniero', 'No', 'Si', 'Si', '1-5', 'M', 'No', 'INNOVADOR', '4', 'Publica '),
(3, 'Mario Gutiérrez Olórtegui', 'UCAL', 'No', 'No', 'Comunicador', 'No', 'Si', 'Si', '1-5', 'M', 'No', 'PROTAGONISTA', '7', 'Privada'),
(4, 'Agueda Benito', 'UPC', 'No', 'No', 'Educadora', 'Si', 'Si', 'Si', '11-15', 'F', 'Si', 'ARQUITECTO', '9', 'Privada'),
(5, 'Alberto Manuel Mori Paredes', 'UNAC', 'Si', 'No', 'Ingeniero', 'No', 'No', 'Si', '16 a mas', 'M', 'No', 'VIRTUOSO', '1', 'Publica '),
(6, 'Andres Velarde Talleri', 'UPN', 'No', 'No', 'Administrador', 'Si', 'No', 'Si', '6-10', 'M', 'No', 'EJECUTIVO', '7', 'Privada'),
(7, 'CACHAY BOZA ORESTES', 'UNMSM', 'No', 'Si', 'Ingeniero', 'Si', 'No', 'Si', '6-10', 'M', 'No', 'ACTIVISTA', '5', 'Publica '),
(8, 'Jorge Alva Hurtado', 'UNI', 'No', 'No', 'Ingeniero', 'Si', 'Si', 'Si', '1-5', 'M', 'No', 'COMANDANTE', '9', 'Publica '),
(9, 'RODRIGUEZ CHAVEZ ELIO IVAN', 'URP', 'No', 'No', 'Abogado', 'Si', 'No', 'Si', '6-10', 'M', 'Si', 'ARQUITECTO', '8', 'Privada'),
(10, 'Pedro Atilio Cotillo Zegarra', 'UNMSM', 'Si', 'No', 'Quimico Farmace', 'No', 'No', 'Si', '6-10', 'M', 'No', 'ACTIVISTA', '2', 'Publica '),
(11, 'Aurelio Padilla Ríos', 'UNI', 'Si', 'No', 'Ingeniero', 'Si', 'Si', 'Si', '6-10', 'M', 'Si', 'MEDIADOR', '2', 'Publica '),
(12, 'Jesús Abel Mejía Marcacuzco', 'UNALM', 'No', 'No', 'Ingeniero', 'Si', 'Si', 'Si', '6-10', 'M', 'No', 'EJECUTIVO', '7', 'Publica '),
(13, 'José María Viaña Pérez', 'UNFV', 'No', 'No', 'Medico', 'Si', 'Si', 'Si', '6-10', 'M', 'No', 'EJECUTIVO', '7', 'Publica '),
(14, 'Freddy Alberto Aponte Guerrero', 'UNE', 'Si', 'No', 'Ingeniero', 'Si', 'Si', 'Si', '11-15', 'M', 'Si', 'MEDIADOR', '1', 'Publica '),
(15, 'Luis Alberto Baldeos Ardían', 'UNJFSC', 'Si', 'No', 'Administrador', 'No', 'Si', 'Si', '6-10', 'M', 'No', 'CONSUL', '2', 'Publica '),
(16, 'Fabiola León Velarde Servetto ', 'UPCH', 'No', 'No', 'Biologa', 'No', 'Si', 'No', 'No experiencia', 'F', 'No', 'ARQUITECTO', '4', 'Privada'),
(17, 'Felipe Portocarrero Suárez', 'UP', 'No', 'No', 'Sociologo', 'Si', 'Si', 'No', 'No experiencia', 'M', 'No', 'EMPRENDEDOR', '5', 'Privada'),
(18, 'Ilse Wisotzki Loli', 'UL', 'No', 'No', 'Filosofo', 'Si', 'Si', 'Si', '6-10', 'M', 'Si', 'PROTAGONISTA', '8', 'Privada'),
(19, 'José Antonio Chang Escobedo', 'USMP', 'No', 'No', 'Ingeniero', 'No', 'Si', 'Si', '11-15', 'M', 'Si', 'AVENTURERO', '3', 'Privada'),
(20, 'Luis Claudio Cervantes Liñán', 'UIGV', 'Si', 'No', 'Psicologo-Aboga', 'Si', 'Si', 'No', 'No experiencia', 'M', 'No', 'DEFENSOR', '2', 'Privada'),
(21, 'Manuel Encarnación Torres Valladares', 'UMA', 'No', 'No', 'Psicologo', 'Si', 'No', 'No', 'No experiencia', 'M', 'No', 'LOGISTA', '4', 'Privada'),
(22, 'Enrique Bedoya Sánchez', 'UTP', 'No', 'No', 'Administrador', 'No', 'Si', 'Si', '16 a mas', 'M', 'No', 'LOGISTA', '6', 'Privada'),
(23, 'Elías Castilla Rosa Pérez', 'UPT', 'No', 'No', 'Educador-escrit', 'Si', 'Si', 'No', 'No experiencia', 'M', 'No', 'LOGISTA', '5', 'Privada'),
(24, 'José Antonio Becerra Ruiz', 'UNAB', 'No', 'No', 'Abogado', 'No', 'Si', 'Si', '1-5', 'M', 'No', 'ANIMADOR', '5', 'Publica '),
(25, 'Humberto C. Llempén Coronel', 'USS', 'No', 'No', 'Ingeniero', 'No', 'No', 'No', 'No experiencia', 'M', 'No', 'LOGICO', '4', 'Privada'),
(26, 'José de la Rosa Cruz Martínez', 'UNT', 'No', 'No', 'Administrador', 'No', 'Si', 'Si', '6-10', 'M', 'No', 'ABOGADO', '6', 'Publica '),
(27, 'Edwin A. Vegas Gallo', 'UNJ', 'No', 'No', 'Biologo-Filosof', 'Si', 'Si', 'No', 'No experiencia', 'M', 'Si', 'ARQUITECTO', '8', 'Publica '),
(28, 'Carroll Douglas Dale Salinas', 'USBC', 'No', 'No', 'Sociologo', 'No', 'Si', 'No', 'No experiencia', 'M', 'No', 'AVENTURERO', '4', 'Privada'),
(29, 'Juan Pablo Moreno Muro', 'UDL', 'No', 'Si', 'Administrador', 'Si', 'No', 'Si', '1-5', 'M', 'No', 'VIRTUOSO', '4', 'Privada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `universidad`
--

CREATE TABLE `universidad` (
  `ID_UNIVERSIDAD` int(11) NOT NULL,
  `NOM_UNIVERSIDAD` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `universidad`
--

INSERT INTO `universidad` (`ID_UNIVERSIDAD`, `NOM_UNIVERSIDAD`) VALUES
(1, 'UNAC'),
(2, 'PUCP');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `candidato`
--
ALTER TABLE `candidato`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_id_univ2` (`ID_UNIVERSIDAD`);

--
-- Indices de la tabla `rectores`
--
ALTER TABLE `rectores`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `universidad`
--
ALTER TABLE `universidad`
  ADD PRIMARY KEY (`ID_UNIVERSIDAD`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `candidato`
--
ALTER TABLE `candidato`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `rectores`
--
ALTER TABLE `rectores`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `universidad`
--
ALTER TABLE `universidad`
  MODIFY `ID_UNIVERSIDAD` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `candidato`
--
ALTER TABLE `candidato`
  ADD CONSTRAINT `fk_id_univ2` FOREIGN KEY (`ID_UNIVERSIDAD`) REFERENCES `universidad` (`ID_UNIVERSIDAD`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
