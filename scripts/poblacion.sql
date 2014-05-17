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

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$12000$hVuMqX9bgF7t$oZ8/Y/P9MAybnfCme6Mz8oXyF/JIy5TVm0mgCYQV/PQ=	2014-05-17 00:34:06.030321-04	t	root	Marcelo Daniel	Franco	marcelodf12@gmail.com	t	t	2014-05-17 00:33:53.23172-04
2	pbkdf2_sha256$12000$Z30I6NYNvGjs$FEnQNv7NjOPWdAysQFPIDURs//Qyvb9Zr01YJDwRNKk=	2014-05-17 00:57:10.10983-04	f	carol	Carolina	Arguello	carol@is2.aps.py	f	t	2014-05-17 00:57:02.107976-04
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

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
8fmcbu3a3s7eg2tgkz0qq3m0zv0h8co6	NGFlZDE5ZmI1NWI4NDAyMTRhODQyMjJlM2IxYjZmYWM3ZGI5MDVjNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-05-31 00:57:10.122-04
\.


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_proyectos (id, nombre, "fechaInicio", "fechaFinP", "fechaFinR", "cantFases", estado, presupuesto, penalizacion, saldo, lider_id) FROM stdin;
2	Proyecto 2	2014-05-12	2014-10-30	\N	3	creado	5000	25	\N	1
3	Proyecto 3	2014-04-12	2013-05-10	\N	4	creado	5000	10	\N	1
1	Proyecto 1	2014-06-16	2014-12-30	\N	4	activo	10000	100	\N	1
4	Proyecto Carol	2014-05-12	2014-11-30	\N	3	creado	3000	10	\N	2
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY fases_fases (id, nombre, "fechaInicioP", "fechaInicioR", estado, proyecto_id, costo, presupuesto, orden) FROM stdin;
12	Fase 1	2014-05-12	\N	creado	4	0	0	1
13	Fase 2	2014-05-12	\N	creado	4	0	0	2
14	Fase 3	2014-05-12	\N	creado	4	0	0	3
8	Fase 1	2014-04-12	\N	creado	3	0	0	1
9	Fase 2	2014-04-12	\N	creado	3	0	0	2
10	Fase 3	2014-04-12	\N	creado	3	0	0	3
11	Fase 4	2014-04-12	\N	creado	3	0	0	4
5	Fase 1	2014-05-12	\N	creado	2	0	0	1
6	Fase 2	2014-05-12	\N	creado	2	0	0	2
7	Fase 3	2014-05-12	\N	creado	2	0	0	3
1	Fase 1	2014-06-16	\N	creado	1	30	0	1
2	Fase 2	2014-06-16	\N	creado	1	85	0	2
3	Fase 3	2014-06-16	\N	creado	1	40	0	3
4	Fase 4	2014-06-16	\N	creado	1	0	0	4
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('fases_fases_id_seq', 14, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_items (id, nombre, "versionAct", estado, complejidad, fase_id, costo) FROM stdin;
3	R3	1	creado	1	1	10
5	Diagrama 2	1	creado	3	2	30
6	Diagrama 3	1	creado	3	2	35
4	Diagrama 1	2	creado	2	2	20
1	R1	2	creado	1	1	10
2	R2	2	creado	1	1	10
7	Clase A	4	creado	3	3	40
8	Diagrama Final	4	creado	4	4	200
\.


--
-- Data for Name: items_atributo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_atributo (id, nombre, descripcion, version, item_id) FROM stdin;
1	Descripcion		1	1
2	Descripcion		1	2
3	Descripcion		1	3
4	Titulo		1	7
5	Responsable		1	7
6	Paquete		1	7
7	Atributo 1	Este es la descripcion	2	4
8	Descripcion	Este es otra descripcion	2	1
9	Descripcion	Esta es la descripcion del primer atributo del item 2	2	2
11	Responsable		2	7
12	Paquete		2	7
10	Titulo	Diagrama Uno	2	7
14	Titulo	Diagrama Uno	3	7
15	Paquete		3	7
13	Responsable	Julio	3	7
17	Responsable	Julio	4	7
18	Titulo	Diagrama Uno	4	7
16	Paquete	Administracion	4	7
19	Titulo		1	8
20	Responsable		1	8
21	Tiempo		1	8
23	Titulo		2	8
24	Responsable		2	8
22	Tiempo	5	2	8
26	Tiempo	5	3	8
27	Responsable		3	8
25	Titulo	Final	3	8
29	Titulo	Final	4	8
30	Tiempo	5	4	8
28	Responsable	Pedro	4	8
\.


--
-- Name: items_atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_atributo_id_seq', 30, true);


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_items_id_seq', 8, true);


--
-- Data for Name: items_relacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_relacion (id, "itemHijo_id", "itemPadre_id", estado) FROM stdin;
2	5	2	t
3	4	3	t
4	6	1	t
5	7	5	t
\.


--
-- Name: items_relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_relacion_id_seq', 5, true);


--
-- Data for Name: items_tipoitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_tipoitem (id, nombre, atributos) FROM stdin;
1	Requerimiento Funcional	(lp0\nVDescripcion\np1\na.
2	Requerimiento No Funcional	(lp0\nVDescripcion\np1\na.
3	Diagrama de Caso de Uso	(lp0\nVTitulo\np1\naVResponsable\np2\naVTiempo\np3\na.
4	Diagrama de Clases	(lp0\nVTitulo\np1\naVResponsable\np2\naVPaquete\np3\na.
\.


--
-- Name: items_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_tipoitem_id_seq', 4, true);


--
-- Data for Name: permisos_permisos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY permisos_permisos (id, permiso, "tipoObjeto", usuario_id, grupo_id, id_fk) FROM stdin;
1	VER	proyecto	1	\N	0
2	ADD	proyecto	1	\N	0
3	VER	proyecto	\N	1	0
4	ADD	proyecto	2	\N	0
\.


--
-- Name: permisos_permisos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('permisos_permisos_id_seq', 4, true);


--
-- Data for Name: proyectos_miembros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_miembros (id, proyecto_id, miembro_id, comite) FROM stdin;
\.


--
-- Name: proyectos_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_miembros_id_seq', 1, false);


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

