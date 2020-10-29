-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 03, 2020 at 07:42 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sastadiet`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add my user', 6, 'add_myuser'),
(22, 'Can change my user', 6, 'change_myuser'),
(23, 'Can delete my user', 6, 'delete_myuser'),
(24, 'Can view my user', 6, 'view_myuser'),
(25, 'Can add contact', 7, 'add_contact'),
(26, 'Can change contact', 7, 'change_contact'),
(27, 'Can delete contact', 7, 'delete_contact'),
(28, 'Can view contact', 7, 'view_contact'),
(29, 'Can add plans', 8, 'add_plans'),
(30, 'Can change plans', 8, 'change_plans'),
(31, 'Can delete plans', 8, 'delete_plans'),
(32, 'Can view plans', 8, 'view_plans'),
(33, 'Can add room', 9, 'add_room'),
(34, 'Can change room', 9, 'change_room'),
(35, 'Can delete room', 9, 'delete_room'),
(36, 'Can view room', 9, 'view_room'),
(37, 'Can add dietitian', 10, 'add_dietitian'),
(38, 'Can change dietitian', 10, 'change_dietitian'),
(39, 'Can delete dietitian', 10, 'delete_dietitian'),
(40, 'Can view dietitian', 10, 'view_dietitian'),
(41, 'Can add messages', 11, 'add_messages'),
(42, 'Can change messages', 11, 'change_messages'),
(43, 'Can delete messages', 11, 'delete_messages'),
(44, 'Can view messages', 11, 'view_messages'),
(45, 'Can add user data', 12, 'add_userdata'),
(46, 'Can change user data', 12, 'change_userdata'),
(47, 'Can delete user data', 12, 'delete_userdata'),
(48, 'Can view user data', 12, 'view_userdata'),
(49, 'Can add room_ member', 13, 'add_room_member'),
(50, 'Can change room_ member', 13, 'change_room_member'),
(51, 'Can delete room_ member', 13, 'delete_room_member'),
(52, 'Can view room_ member', 13, 'view_room_member'),
(53, 'Can add payment', 14, 'add_payment'),
(54, 'Can change payment', 14, 'change_payment'),
(55, 'Can delete payment', 14, 'delete_payment'),
(56, 'Can view payment', 14, 'view_payment'),
(57, 'Can add meeting', 15, 'add_meeting'),
(58, 'Can change meeting', 15, 'change_meeting'),
(59, 'Can delete meeting', 15, 'delete_meeting'),
(60, 'Can view meeting', 15, 'view_meeting'),
(61, 'Can add feedback', 16, 'add_feedback'),
(62, 'Can change feedback', 16, 'change_feedback'),
(63, 'Can delete feedback', 16, 'delete_feedback'),
(64, 'Can view feedback', 16, 'view_feedback'),
(65, 'Can add poster', 17, 'add_poster'),
(66, 'Can change poster', 17, 'change_poster'),
(67, 'Can delete poster', 17, 'delete_poster'),
(68, 'Can view poster', 17, 'view_poster'),
(69, 'Can add user health data', 18, 'add_userhealthdata'),
(70, 'Can change user health data', 18, 'change_userhealthdata'),
(71, 'Can delete user health data', 18, 'delete_userhealthdata'),
(72, 'Can view user health data', 18, 'view_userhealthdata'),
(73, 'Can add workout_type', 19, 'add_workout_type'),
(74, 'Can change workout_type', 19, 'change_workout_type'),
(75, 'Can delete workout_type', 19, 'delete_workout_type'),
(76, 'Can view workout_type', 19, 'view_workout_type'),
(77, 'Can add week_ report', 20, 'add_week_report'),
(78, 'Can change week_ report', 20, 'change_week_report'),
(79, 'Can delete week_ report', 20, 'delete_week_report'),
(80, 'Can view week_ report', 20, 'view_week_report'),
(81, 'Can add cron job log', 21, 'add_cronjoblog'),
(82, 'Can change cron job log', 21, 'change_cronjoblog'),
(83, 'Can delete cron job log', 21, 'delete_cronjoblog'),
(84, 'Can view cron job log', 21, 'view_cronjoblog');

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_contact`
--

CREATE TABLE `diet_app_contact` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `message` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_dietitian`
--

CREATE TABLE `diet_app_dietitian` (
  `user_id` int(11) NOT NULL,
  `firstname` varchar(10) NOT NULL,
  `middlename` varchar(10) NOT NULL,
  `lastname` varchar(10) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `qualification` varchar(10) NOT NULL,
  `image` varchar(100) NOT NULL,
  `commission_smartplan` decimal(5,2) NOT NULL,
  `commission_smartplan_healthIssue` decimal(5,2) NOT NULL,
  `commission_smartplusplan_healthissue` decimal(5,2) NOT NULL,
  `commission_smartplusplan` decimal(5,2) NOT NULL,
  `revenue` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diet_app_dietitian`
--

INSERT INTO `diet_app_dietitian` (`user_id`, `firstname`, `middlename`, `lastname`, `mobile_no`, `qualification`, `image`, `commission_smartplan`, `commission_smartplan_healthIssue`, `commission_smartplusplan_healthissue`, `commission_smartplusplan`, `revenue`) VALUES
(2, 'Umesh', 'V', 'Kachariya', '9967112200', 'MCA', 'diet_app/avatar_qP00xoa.png', '50.00', '60.00', '80.00', '70.00', '0.00'),
(3, 'Rajesh', 'K', 'Patel', '9956712345', 'BCA', 'diet_app/avatar_pt6TTXT.png', '40.00', '50.00', '70.00', '60.00', '0.00'),
(4, 'Kevin', 'k', 'Savaliya', '9546812349', 'BCA', 'diet_app/avatar_f8B4X2d.png', '30.00', '40.00', '60.00', '50.00', '0.00');

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_feedback`
--

CREATE TABLE `diet_app_feedback` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `review` varchar(300) NOT NULL,
  `datetime` datetime(6) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_meeting`
--

CREATE TABLE `diet_app_meeting` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `type` varchar(70) NOT NULL,
  `room_id` int(11) DEFAULT NULL,
  `dietitian_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `end_time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_messages`
--

CREATE TABLE `diet_app_messages` (
  `id` int(11) NOT NULL,
  `text` varchar(500) NOT NULL,
  `sender` varchar(100) NOT NULL,
  `room_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_myuser`
--

CREATE TABLE `diet_app_myuser` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `username` varchar(15) NOT NULL,
  `is_customer` tinyint(1) NOT NULL,
  `is_dietitian` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `ref_key` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diet_app_myuser`
--

INSERT INTO `diet_app_myuser` (`password`, `last_login`, `is_superuser`, `id`, `email`, `username`, `is_customer`, `is_dietitian`, `is_admin`, `is_staff`, `is_active`, `ref_key`) VALUES
('pbkdf2_sha256$180000$r3bDhQgT8hXE$dWblge7YeLx/CwGOBf325lih0UGFc+3SYTtAx5cojfo=', '2020-10-03 15:36:50.973447', 1, 1, 'abc@gmail.com', 'sastadiet', 0, 0, 1, 1, 1, '!ev6Kh519bB8UzbQuDJIQg52onyEcjWHTqXzRLNOU'),
('8935', '2020-10-03 16:50:15.000000', 0, 2, 'xyz@gmail.com', 'Umesh19', 0, 1, 0, 0, 1, ''),
('Rajesh', '2020-10-03 16:51:23.000000', 0, 3, 'rajs11@gmail.com', 'Rajesh12', 0, 1, 0, 0, 1, ''),
('9090', '2020-10-03 16:52:43.000000', 0, 4, 'Kevin@gmail.com', 'Kevin47', 0, 1, 0, 0, 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_myuser_groups`
--

CREATE TABLE `diet_app_myuser_groups` (
  `id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_myuser_user_permissions`
--

CREATE TABLE `diet_app_myuser_user_permissions` (
  `id` int(11) NOT NULL,
  `myuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_payment`
--

CREATE TABLE `diet_app_payment` (
  `id` int(11) NOT NULL,
  `transaction_id` varchar(200) NOT NULL,
  `amount` decimal(5,2) NOT NULL,
  `plan_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_plans`
--

CREATE TABLE `diet_app_plans` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `price` double NOT NULL,
  `is_plusplan` tinyint(1) NOT NULL,
  `is_healthissue` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diet_app_plans`
--

INSERT INTO `diet_app_plans` (`id`, `title`, `description`, `price`, `is_plusplan`, `is_healthissue`) VALUES
(1, 'SMART PLAN', 'customized diet chart, workout chart, Healthy Recipe ,workout videos ,Support', 299, 0, 0),
(2, 'SMART + PLAN', 'customized diet chart, workout chart, Healthy Recipe, workout videos ,Chat With Coach ,4 calls per month', 399, 1, 0),
(3, 'SMART PLAN FOR HEALTH ISSUES', 'customized diet chart, workout chart ,Healthy Recipe ,workout videos ,Support', 499, 0, 1),
(4, 'SMART + PLAN FOR HEALTH ISSUES', 'customized diet chart ,workout chart ,Healthy Recipe, workout videos ,Chat With Coach ,4 calls per month', 599, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_poster`
--

CREATE TABLE `diet_app_poster` (
  `id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `diet_app_poster`
--

INSERT INTO `diet_app_poster` (`id`, `image`, `name`) VALUES
(1, 'diet_app/chatback.jpg', 'Poster1'),
(2, 'diet_app/plans-bg_wHvpZnQ.jpg', 'Poster2');

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_room`
--

CREATE TABLE `diet_app_room` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `created_by` varchar(100) NOT NULL,
  `created_at` date DEFAULT NULL,
  `meeting_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_room_member`
--

CREATE TABLE `diet_app_room_member` (
  `id` int(11) NOT NULL,
  `is_member` tinyint(1) NOT NULL,
  `added_by` varchar(40) NOT NULL,
  `room_id` int(11) NOT NULL,
  `username_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_userdata`
--

CREATE TABLE `diet_app_userdata` (
  `user_id` int(11) NOT NULL,
  `firstname` varchar(10) NOT NULL,
  `middlename` varchar(10) NOT NULL,
  `lastname` varchar(10) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(11) NOT NULL,
  `height` decimal(5,2) NOT NULL,
  `weight` decimal(5,2) NOT NULL,
  `mobile_no` varchar(10) NOT NULL,
  `city` varchar(500) NOT NULL,
  `created_at` date DEFAULT NULL,
  `updates_at` date DEFAULT NULL,
  `date_tofill_form` date DEFAULT NULL,
  `plan_end_date` date DEFAULT NULL,
  `call_count` int(11) DEFAULT NULL,
  `is_data_filled` tinyint(1) NOT NULL,
  `is_chart_sent` tinyint(1) NOT NULL,
  `payment_uuid` varchar(200) DEFAULT NULL,
  `dietitian_id` int(11) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  `is_feed_remain` tinyint(1) NOT NULL,
  `is_paid` tinyint(1) NOT NULL,
  `plan_buy_count` int(11) NOT NULL,
  `points` decimal(5,2) NOT NULL,
  `referral_code` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_userhealthdata`
--

CREATE TABLE `diet_app_userhealthdata` (
  `userdata_id` int(11) NOT NULL,
  `workout` tinyint(1) NOT NULL,
  `workout_time` varchar(15) NOT NULL,
  `workout_time_inday` varchar(20) NOT NULL,
  `workout_day_inweek` varchar(20) NOT NULL,
  `want_to_achive` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `dishes` varchar(30) NOT NULL,
  `have_disease` tinyint(1) NOT NULL,
  `supplements` varchar(200) NOT NULL,
  `about` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_week_report`
--

CREATE TABLE `diet_app_week_report` (
  `id` int(11) NOT NULL,
  `old_weight` decimal(5,2) NOT NULL,
  `new_weight` decimal(5,2) DEFAULT NULL,
  `query` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `diet_app_workout_type`
--

CREATE TABLE `diet_app_workout_type` (
  `id` int(11) NOT NULL,
  `type` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-10-03 15:38:57.798419', '1', 'diet_app/chatback.jpg', 1, '[{\"added\": {}}]', 17, 1),
(2, '2020-10-03 15:39:11.276677', '2', 'diet_app/plans-bg_wHvpZnQ.jpg', 1, '[{\"added\": {}}]', 17, 1),
(3, '2020-10-03 16:50:30.565453', '2', 'Umesh19', 1, '[{\"added\": {}}]', 6, 1),
(4, '2020-10-03 16:51:09.115945', '2', 'Umesh', 1, '[{\"added\": {}}]', 10, 1),
(5, '2020-10-03 16:51:37.560842', '3', 'Rajesh12', 1, '[{\"added\": {}}]', 6, 1),
(6, '2020-10-03 16:52:08.336689', '3', 'Rajesh', 1, '[{\"added\": {}}]', 10, 1),
(7, '2020-10-03 16:52:56.672101', '4', 'Kevin47', 1, '[{\"added\": {}}]', 6, 1),
(8, '2020-10-03 16:53:22.861456', '4', 'Kevin', 1, '[{\"added\": {}}]', 10, 1),
(9, '2020-10-03 16:56:17.724534', '1', 'SMART PLAN', 1, '[{\"added\": {}}]', 8, 1),
(10, '2020-10-03 16:56:35.765366', '2', 'SMART + PLAN', 1, '[{\"added\": {}}]', 8, 1),
(11, '2020-10-03 16:56:53.870720', '3', 'SMART PLAN FOR HEALTH ISSUES', 1, '[{\"added\": {}}]', 8, 1),
(12, '2020-10-03 16:57:16.766520', '4', 'SMART + PLAN FOR HEALTH ISSUES', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(7, 'diet_app', 'contact'),
(10, 'diet_app', 'dietitian'),
(16, 'diet_app', 'feedback'),
(15, 'diet_app', 'meeting'),
(11, 'diet_app', 'messages'),
(6, 'diet_app', 'myuser'),
(14, 'diet_app', 'payment'),
(8, 'diet_app', 'plans'),
(17, 'diet_app', 'poster'),
(9, 'diet_app', 'room'),
(13, 'diet_app', 'room_member'),
(12, 'diet_app', 'userdata'),
(18, 'diet_app', 'userhealthdata'),
(20, 'diet_app', 'week_report'),
(19, 'diet_app', 'workout_type'),
(21, 'django_cron', 'cronjoblog'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_cron_cronjoblog`
--

CREATE TABLE `django_cron_cronjoblog` (
  `id` int(11) NOT NULL,
  `code` varchar(64) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `is_success` tinyint(1) NOT NULL,
  `message` longtext NOT NULL,
  `ran_at_time` time(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-10-03 15:27:22.277508'),
(2, 'contenttypes', '0002_remove_content_type_name', '2020-10-03 15:27:23.173161'),
(3, 'auth', '0001_initial', '2020-10-03 15:27:23.950714'),
(4, 'auth', '0002_alter_permission_name_max_length', '2020-10-03 15:27:27.355113'),
(5, 'auth', '0003_alter_user_email_max_length', '2020-10-03 15:27:27.417157'),
(6, 'auth', '0004_alter_user_username_opts', '2020-10-03 15:27:27.465191'),
(7, 'auth', '0005_alter_user_last_login_null', '2020-10-03 15:27:27.507222'),
(8, 'auth', '0006_require_contenttypes_0002', '2020-10-03 15:27:27.545248'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2020-10-03 15:27:27.582278'),
(10, 'auth', '0008_alter_user_username_max_length', '2020-10-03 15:27:27.629327'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2020-10-03 15:27:27.686348'),
(12, 'auth', '0010_alter_group_name_max_length', '2020-10-03 15:27:28.070622'),
(13, 'auth', '0011_update_proxy_permissions', '2020-10-03 15:27:28.151680'),
(14, 'diet_app', '0001_initial', '2020-10-03 15:27:30.781546'),
(15, 'admin', '0001_initial', '2020-10-03 15:27:51.911966'),
(16, 'admin', '0002_logentry_remove_auto_add', '2020-10-03 15:27:56.454401'),
(17, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-03 15:27:56.901704'),
(18, 'diet_app', '0002_auto_20201003_2057', '2020-10-03 15:28:11.781297'),
(19, 'django_cron', '0001_initial', '2020-10-03 15:28:16.473599'),
(20, 'django_cron', '0002_remove_max_length_from_CronJobLog_message', '2020-10-03 15:28:18.077738'),
(21, 'sessions', '0001_initial', '2020-10-03 15:28:18.442026');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `diet_app_contact`
--
ALTER TABLE `diet_app_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diet_app_dietitian`
--
ALTER TABLE `diet_app_dietitian`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `diet_app_feedback`
--
ALTER TABLE `diet_app_feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diet_app_meeting`
--
ALTER TABLE `diet_app_meeting`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_meeting_user_id_49d89eaa_fk_diet_app_userdata_user_id` (`user_id`),
  ADD KEY `diet_app_meeting_dietitian_id_23257dae_fk_diet_app_` (`dietitian_id`);

--
-- Indexes for table `diet_app_messages`
--
ALTER TABLE `diet_app_messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_messages_room_id_id_f2eb29f6_fk_diet_app_room_id` (`room_id_id`);

--
-- Indexes for table `diet_app_myuser`
--
ALTER TABLE `diet_app_myuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `diet_app_myuser_groups`
--
ALTER TABLE `diet_app_myuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `diet_app_myuser_groups_myuser_id_group_id_a5ed327a_uniq` (`myuser_id`,`group_id`),
  ADD KEY `diet_app_myuser_groups_group_id_7230e8e1_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `diet_app_myuser_user_permissions`
--
ALTER TABLE `diet_app_myuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `diet_app_myuser_user_per_myuser_id_permission_id_0980030b_uniq` (`myuser_id`,`permission_id`),
  ADD KEY `diet_app_myuser_user_permission_id_0d7edfc4_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `diet_app_payment`
--
ALTER TABLE `diet_app_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_payment_user_id_id_1a57148b_fk_diet_app_` (`user_id_id`),
  ADD KEY `diet_app_payment_plan_id_id_ea9d7291_fk_diet_app_plans_id` (`plan_id_id`);

--
-- Indexes for table `diet_app_plans`
--
ALTER TABLE `diet_app_plans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diet_app_poster`
--
ALTER TABLE `diet_app_poster`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diet_app_room`
--
ALTER TABLE `diet_app_room`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_room_meeting_id_b1e4b6cf_fk_diet_app_meeting_id` (`meeting_id`);

--
-- Indexes for table `diet_app_room_member`
--
ALTER TABLE `diet_app_room_member`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_room_member_room_id_46b75299_fk_diet_app_room_id` (`room_id`),
  ADD KEY `diet_app_room_member_username_id_b8d1688f_fk_diet_app_` (`username_id`);

--
-- Indexes for table `diet_app_userdata`
--
ALTER TABLE `diet_app_userdata`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `diet_app_userdata_dietitian_id_58ea3503_fk_diet_app_` (`dietitian_id`),
  ADD KEY `diet_app_userdata_plan_id_aa31bbf2_fk_diet_app_plans_id` (`plan_id`);

--
-- Indexes for table `diet_app_userhealthdata`
--
ALTER TABLE `diet_app_userhealthdata`
  ADD PRIMARY KEY (`userdata_id`);

--
-- Indexes for table `diet_app_week_report`
--
ALTER TABLE `diet_app_week_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_week_report_user_id_9058e376_fk_diet_app_` (`user_id`);

--
-- Indexes for table `diet_app_workout_type`
--
ALTER TABLE `diet_app_workout_type`
  ADD PRIMARY KEY (`id`),
  ADD KEY `diet_app_workout_typ_user_id_f78e00ae_fk_diet_app_` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_cron_cronjoblog`
--
ALTER TABLE `django_cron_cronjoblog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_cron_cronjoblog_code_is_success_ran_at_time_84da9606_idx` (`code`,`is_success`,`ran_at_time`),
  ADD KEY `django_cron_cronjoblog_code_start_time_ran_at_time_8b50b8fa_idx` (`code`,`start_time`,`ran_at_time`),
  ADD KEY `django_cron_cronjoblog_code_start_time_4fc78f9d_idx` (`code`,`start_time`),
  ADD KEY `django_cron_cronjoblog_code_48865653` (`code`),
  ADD KEY `django_cron_cronjoblog_start_time_d68c0dd9` (`start_time`),
  ADD KEY `django_cron_cronjoblog_end_time_7918602a` (`end_time`),
  ADD KEY `django_cron_cronjoblog_ran_at_time_7fed2751` (`ran_at_time`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `diet_app_contact`
--
ALTER TABLE `diet_app_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_feedback`
--
ALTER TABLE `diet_app_feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_meeting`
--
ALTER TABLE `diet_app_meeting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_messages`
--
ALTER TABLE `diet_app_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_myuser`
--
ALTER TABLE `diet_app_myuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `diet_app_myuser_groups`
--
ALTER TABLE `diet_app_myuser_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_myuser_user_permissions`
--
ALTER TABLE `diet_app_myuser_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_payment`
--
ALTER TABLE `diet_app_payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_plans`
--
ALTER TABLE `diet_app_plans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `diet_app_poster`
--
ALTER TABLE `diet_app_poster`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `diet_app_room`
--
ALTER TABLE `diet_app_room`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_room_member`
--
ALTER TABLE `diet_app_room_member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_week_report`
--
ALTER TABLE `diet_app_week_report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diet_app_workout_type`
--
ALTER TABLE `diet_app_workout_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `django_cron_cronjoblog`
--
ALTER TABLE `django_cron_cronjoblog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `diet_app_dietitian`
--
ALTER TABLE `diet_app_dietitian`
  ADD CONSTRAINT `diet_app_dietitian_user_id_c5554ac9_fk_diet_app_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `diet_app_myuser` (`id`);

--
-- Constraints for table `diet_app_meeting`
--
ALTER TABLE `diet_app_meeting`
  ADD CONSTRAINT `diet_app_meeting_dietitian_id_23257dae_fk_diet_app_` FOREIGN KEY (`dietitian_id`) REFERENCES `diet_app_dietitian` (`user_id`),
  ADD CONSTRAINT `diet_app_meeting_user_id_49d89eaa_fk_diet_app_userdata_user_id` FOREIGN KEY (`user_id`) REFERENCES `diet_app_userdata` (`user_id`);

--
-- Constraints for table `diet_app_messages`
--
ALTER TABLE `diet_app_messages`
  ADD CONSTRAINT `diet_app_messages_room_id_id_f2eb29f6_fk_diet_app_room_id` FOREIGN KEY (`room_id_id`) REFERENCES `diet_app_room` (`id`);

--
-- Constraints for table `diet_app_myuser_groups`
--
ALTER TABLE `diet_app_myuser_groups`
  ADD CONSTRAINT `diet_app_myuser_groups_group_id_7230e8e1_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `diet_app_myuser_groups_myuser_id_e5a4f209_fk_diet_app_myuser_id` FOREIGN KEY (`myuser_id`) REFERENCES `diet_app_myuser` (`id`);

--
-- Constraints for table `diet_app_myuser_user_permissions`
--
ALTER TABLE `diet_app_myuser_user_permissions`
  ADD CONSTRAINT `diet_app_myuser_user_myuser_id_39d58a01_fk_diet_app_` FOREIGN KEY (`myuser_id`) REFERENCES `diet_app_myuser` (`id`),
  ADD CONSTRAINT `diet_app_myuser_user_permission_id_0d7edfc4_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `diet_app_payment`
--
ALTER TABLE `diet_app_payment`
  ADD CONSTRAINT `diet_app_payment_plan_id_id_ea9d7291_fk_diet_app_plans_id` FOREIGN KEY (`plan_id_id`) REFERENCES `diet_app_plans` (`id`),
  ADD CONSTRAINT `diet_app_payment_user_id_id_1a57148b_fk_diet_app_` FOREIGN KEY (`user_id_id`) REFERENCES `diet_app_userdata` (`user_id`);

--
-- Constraints for table `diet_app_room`
--
ALTER TABLE `diet_app_room`
  ADD CONSTRAINT `diet_app_room_meeting_id_b1e4b6cf_fk_diet_app_meeting_id` FOREIGN KEY (`meeting_id`) REFERENCES `diet_app_meeting` (`id`);

--
-- Constraints for table `diet_app_room_member`
--
ALTER TABLE `diet_app_room_member`
  ADD CONSTRAINT `diet_app_room_member_room_id_46b75299_fk_diet_app_room_id` FOREIGN KEY (`room_id`) REFERENCES `diet_app_room` (`id`),
  ADD CONSTRAINT `diet_app_room_member_username_id_b8d1688f_fk_diet_app_` FOREIGN KEY (`username_id`) REFERENCES `diet_app_userdata` (`user_id`);

--
-- Constraints for table `diet_app_userdata`
--
ALTER TABLE `diet_app_userdata`
  ADD CONSTRAINT `diet_app_userdata_dietitian_id_58ea3503_fk_diet_app_` FOREIGN KEY (`dietitian_id`) REFERENCES `diet_app_dietitian` (`user_id`),
  ADD CONSTRAINT `diet_app_userdata_plan_id_aa31bbf2_fk_diet_app_plans_id` FOREIGN KEY (`plan_id`) REFERENCES `diet_app_plans` (`id`),
  ADD CONSTRAINT `diet_app_userdata_user_id_1a16e478_fk_diet_app_myuser_id` FOREIGN KEY (`user_id`) REFERENCES `diet_app_myuser` (`id`);

--
-- Constraints for table `diet_app_userhealthdata`
--
ALTER TABLE `diet_app_userhealthdata`
  ADD CONSTRAINT `diet_app_userhealthd_userdata_id_1f90b4ff_fk_diet_app_` FOREIGN KEY (`userdata_id`) REFERENCES `diet_app_userdata` (`user_id`);

--
-- Constraints for table `diet_app_week_report`
--
ALTER TABLE `diet_app_week_report`
  ADD CONSTRAINT `diet_app_week_report_user_id_9058e376_fk_diet_app_` FOREIGN KEY (`user_id`) REFERENCES `diet_app_userdata` (`user_id`);

--
-- Constraints for table `diet_app_workout_type`
--
ALTER TABLE `diet_app_workout_type`
  ADD CONSTRAINT `diet_app_workout_typ_user_id_f78e00ae_fk_diet_app_` FOREIGN KEY (`user_id`) REFERENCES `diet_app_userhealthdata` (`userdata_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
