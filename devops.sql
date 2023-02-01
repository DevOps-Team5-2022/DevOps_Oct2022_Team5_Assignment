-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 25, 2023 at 12:53 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10
USE devops;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `devops`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `CompanyID` int(4) NOT NULL,
  `CompanyName` varchar(50) NOT NULL,
  `JobRole` varchar(50) NOT NULL,
  `CompanyContact` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`CompanyID`, `CompanyName`, `JobRole`, `CompanyContact`, `Email`) VALUES
(1, 'Company A', 'Software Developer', 'Mr A', 'killmyselfDevops@gmail.com'),
(2, 'Company B', 'Software QA', 'Ms B', 'killmyselfDevops@gmail.com'),
(3, 'Company C', 'Intern', 'Mdm C', 'killmyselfDevops@gmail.com'),
(4, 'Company D', 'Documentation Intern', 'Mdm C', 'killmyselfDevops@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `StudentID` char(10) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Preference` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`StudentID`, `Name`, `Preference`, `Status`) VALUES
('S12345670A', 'Student 1', 'Software Development', 'Unassigned'),
('S12345671B', 'Student 2', 'System Development', 'Unassigned'),
('S12345672C', 'Student 3', 'Software Engineering, Development', 'Unassigned'),
('S12345673D', 'Student 4', 'IOS and Android Development', 'Unassigned'),
('S12345674E', 'Student 5', 'Documents, QA Testing and Development', 'Unassigned'),
('S12345675F', 'Student 6', 'Software Engineering, Development', 'Unassigned'),
('S12345676G', 'Student 7', 'IOS and Android Development', 'Unassigned');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`CompanyID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `CompanyID` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
