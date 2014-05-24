--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
1	Administradores
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	proyectos	proyectos	proyectos
8	miembros	proyectos	miembros
9	items	items	items
10	relacion	items	relacion
11	atributo	items	atributo
12	tipo item	items	tipoitem
13	fases	fases	fases
14	permisos	permisos	permisos
15	lineas base	lineasBase	lineasbase
16	relacion item linea base	lineasBase	relacionitemlineabase
17	solicitud cambio	solicitudCambio	solicitudcambio
18	votos	solicitudCambio	votos
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add proyectos	7	add_proyectos
20	Can change proyectos	7	change_proyectos
21	Can delete proyectos	7	delete_proyectos
22	Can add miembros	8	add_miembros
23	Can change miembros	8	change_miembros
24	Can delete miembros	8	delete_miembros
25	Can add items	9	add_items
26	Can change items	9	change_items
27	Can delete items	9	delete_items
28	Can add relacion	10	add_relacion
29	Can change relacion	10	change_relacion
30	Can delete relacion	10	delete_relacion
31	Can add atributo	11	add_atributo
32	Can change atributo	11	change_atributo
33	Can delete atributo	11	delete_atributo
34	Can add tipo item	12	add_tipoitem
35	Can change tipo item	12	change_tipoitem
36	Can delete tipo item	12	delete_tipoitem
37	Can add fases	13	add_fases
38	Can change fases	13	change_fases
39	Can delete fases	13	delete_fases
40	Can add permisos	14	add_permisos
41	Can change permisos	14	change_permisos
42	Can delete permisos	14	delete_permisos
43	Can add lineas base	15	add_lineasbase
44	Can change lineas base	15	change_lineasbase
45	Can delete lineas base	15	delete_lineasbase
46	Can add relacion item linea base	16	add_relacionitemlineabase
47	Can change relacion item linea base	16	change_relacionitemlineabase
48	Can delete relacion item linea base	16	delete_relacionitemlineabase
49	Can add solicitud cambio	17	add_solicitudcambio
50	Can change solicitud cambio	17	change_solicitudcambio
51	Can delete solicitud cambio	17	delete_solicitudcambio
52	Can add votos	18	add_votos
53	Can change votos	18	change_votos
54	Can delete votos	18	delete_votos
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 54, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$12000$Z30I6NYNvGjs$FEnQNv7NjOPWdAysQFPIDURs//Qyvb9Zr01YJDwRNKk=	2014-05-23 22:58:28.609299-04	f	carol	Carolina	Arguello	carol@is2.aps.py	f	t	2014-05-17 00:57:02.107976-04
1	pbkdf2_sha256$12000$hVuMqX9bgF7t$oZ8/Y/P9MAybnfCme6Mz8oXyF/JIy5TVm0mgCYQV/PQ=	2014-05-23 23:28:00.321927-04	t	root	Marcelo Daniel	Franco	marcelodf12@gmail.com	t	t	2014-05-17 00:33:53.23172-04
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 2, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 18, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
8fmcbu3a3s7eg2tgkz0qq3m0zv0h8co6	NGFlZDE5ZmI1NWI4NDAyMTRhODQyMjJlM2IxYjZmYWM3ZGI5MDVjNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-05-31 00:57:10.122-04
evzc4sqypflum6piywcubdtihvbisy4f	ZDRjNjYzN2NmMWJhMjNiYTBjZjZhODgwMmU2MmIzZDE0YWRjMDFiOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-03 08:24:25.638827-04
leehpvn109pza20j3durkh6e22ukt1fr	ZDRjNjYzN2NmMWJhMjNiYTBjZjZhODgwMmU2MmIzZDE0YWRjMDFiOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-06 23:28:00.333838-04
\.


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_proyectos (id, nombre, "fechaInicio", "fechaFinP", "fechaFinR", "cantFases", estado, presupuesto, penalizacion, saldo, lider_id) FROM stdin;
7	Proyecto 2	2014-05-12	2015-12-12	\N	6	creado	3000	10	\N	2
6	Proyecto 1	2014-05-12	2014-12-12	\N	4	activo	10000	100	\N	2
8	Proyecto 3	2013-03-10	2015-12-12	\N	3	creado	5000	6	\N	1
9	Proyecto 5	2013-03-10	2013-03-21	\N	4	activo	5000	10	\N	1
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY fases_fases (id, nombre, "fechaInicioP", "fechaInicioR", estado, proyecto_id, costo, presupuesto, orden) FROM stdin;
23	Fase 1	2014-05-12	\N	creado	7	0	0	1
24	Fase 2	2014-05-12	\N	creado	7	0	0	2
25	Fase 3	2014-05-12	\N	creado	7	0	0	3
26	Fase 4	2014-05-12	\N	creado	7	0	0	4
27	Fase 5	2014-05-12	\N	creado	7	0	0	5
28	Fase 6	2014-05-12	\N	creado	7	0	0	6
19	Fase 1	2014-05-12	\N	creado	6	30	0	1
20	Fase 2	2014-05-12	\N	creado	6	10	0	2
21	Fase 3	2014-05-12	\N	creado	6	10	0	3
22	Fase 4	2014-05-12	\N	creado	6	0	0	4
29	Fase 1	2013-03-10	\N	creado	8	0	0	1
30	Fase 2	2013-03-10	\N	creado	8	0	0	2
31	Fase 3	2013-03-10	\N	creado	8	0	0	3
32	Fase 1	2013-03-10	\N	creado	9	0	0	1
33	Fase 2	2013-03-10	\N	creado	9	0	0	2
34	Fase 3	2013-03-10	\N	creado	9	0	0	3
35	Fase 4	2013-03-10	\N	creado	9	0	0	4
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('fases_fases_id_seq', 35, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_items (id, nombre, "versionAct", estado, complejidad, fase_id, costo) FROM stdin;
15	Item 2	1	creado	1	19	10
17	Item 4	1	creado	1	20	10
18	Item 5	1	creado	3	21	10
16	Item 3	1	finalizado	1	19	10
14	Item 1	1	finalizado	1	19	10
\.


--
-- Data for Name: items_atributo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_atributo (id, nombre, descripcion, version, item_id) FROM stdin;
\.


--
-- Name: items_atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_atributo_id_seq', 1, false);


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_items_id_seq', 18, true);


--
-- Data for Name: items_relacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_relacion (id, "itemHijo_id", "itemPadre_id", estado) FROM stdin;
10	16	14	t
11	17	15	t
12	18	17	t
\.


--
-- Name: items_relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_relacion_id_seq', 12, true);


--
-- Data for Name: items_tipoitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_tipoitem (id, nombre, atributos) FROM stdin;
\.


--
-- Name: items_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_tipoitem_id_seq', 4, true);


--
-- Data for Name: lineasBase_lineasbase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "lineasBase_lineasbase" (id, nombre, estado, fase_id) FROM stdin;
8	L1	cerrado	19
\.


--
-- Name: lineasBase_lineasbase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineasBase_lineasbase_id_seq"', 8, true);


--
-- Data for Name: lineasBase_relacionitemlineabase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "lineasBase_relacionitemlineabase" (id, item_id, linea_id) FROM stdin;
8	16	8
9	14	8
\.


--
-- Name: lineasBase_relacionitemlineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineasBase_relacionitemlineabase_id_seq"', 9, true);


--
-- Data for Name: permisos_permisos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY permisos_permisos (id, permiso, "tipoObjeto", usuario_id, grupo_id, id_fk) FROM stdin;
6	VER	proyecto	\N	\N	0
7	ADD	proyecto	1	\N	0
8	VER	proyecto	1	\N	0
9	VER	proyecto	2	\N	0
10	ADD	proyecto	2	\N	0
\.


--
-- Name: permisos_permisos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('permisos_permisos_id_seq', 10, true);


--
-- Data for Name: proyectos_miembros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_miembros (id, proyecto_id, miembro_id, comite) FROM stdin;
3	6	1	t
\.


--
-- Name: proyectos_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_miembros_id_seq', 3, true);


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 9, true);


--
-- Data for Name: solicitudCambio_solicitudcambio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "solicitudCambio_solicitudcambio" (id, descripcion, "fechaExpiracion", "lineaBase_id", item_id, "costoAdicional", estado, orden, usuario_id) FROM stdin;
\.


--
-- Name: solicitudCambio_solicitudcambio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_solicitudcambio_id_seq"', 3, true);


--
-- Data for Name: solicitudCambio_votos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "solicitudCambio_votos" (id, solicitud_id, estado, usuario_id, aceptar) FROM stdin;
\.


--
-- Name: solicitudCambio_votos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_votos_id_seq"', 4, true);


--
-- PostgreSQL database dump complete
--

