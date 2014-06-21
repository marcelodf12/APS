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
1	pbkdf2_sha256$12000$hVuMqX9bgF7t$oZ8/Y/P9MAybnfCme6Mz8oXyF/JIy5TVm0mgCYQV/PQ=	2014-06-20 22:38:40.304332-04	t	root	Marcelo Daniel	Franco	marcelodf12@gmail.com	t	t	2014-05-17 00:33:53.23172-04
2	pbkdf2_sha256$12000$Z30I6NYNvGjs$FEnQNv7NjOPWdAysQFPIDURs//Qyvb9Zr01YJDwRNKk=	2014-06-20 22:39:00.872568-04	f	carol	Carolina	Arguello	carol@is2.aps.py	f	t	2014-05-17 00:57:02.107976-04
3	pbkdf2_sha256$12000$GZHdSk6yW6eU$+jIyIdN0/jBmI/S2RY6tqLcTyJpG1qqsblu1kzI1x04=	2014-06-06 21:15:45.873343-04	f	marce	Marcelo	Franco	marcelo12@gmail.com	f	t	2014-06-06 21:15:32.694428-04
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

SELECT pg_catalog.setval('auth_user_id_seq', 3, true);


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
wezq4ssjqp29v8scuvife14v2mesh59n	NGFlZDE5ZmI1NWI4NDAyMTRhODQyMjJlM2IxYjZmYWM3ZGI5MDVjNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-06-07 09:32:06.440789-04
k6g3h0pzcyefwz8gqmbe735si9qlnoh6	ZDRjNjYzN2NmMWJhMjNiYTBjZjZhODgwMmU2MmIzZDE0YWRjMDFiOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-07 09:57:59.655494-04
btjhy3dgmitp41eihm5aa7l57ps9v8ts	ZDRjNjYzN2NmMWJhMjNiYTBjZjZhODgwMmU2MmIzZDE0YWRjMDFiOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-08 15:44:05.737521-04
c79sxs61cdku04vf9j8swj6ygz6osmzi	ZDRjNjYzN2NmMWJhMjNiYTBjZjZhODgwMmU2MmIzZDE0YWRjMDFiOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=	2014-06-20 21:26:05.240077-04
qks1wkc309n3lbvj10cz1i1d58qzawq0	NGFlZDE5ZmI1NWI4NDAyMTRhODQyMjJlM2IxYjZmYWM3ZGI5MDVjNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=	2014-07-04 22:39:00.88413-04
\.


--
-- Data for Name: proyectos_proyectos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_proyectos (id, nombre, "fechaInicio", "fechaFinP", "fechaFinR", "cantFases", estado, presupuesto, penalizacion, saldo, lider_id) FROM stdin;
6	Proyecto 1	2014-05-12	2014-12-12	2014-06-07	4	finalizado	10000	0	9940	2
9	Proyecto 5	2013-03-10	2013-03-21	\N	4	activo	5000	10	320	1
11	Proyecto de Prueba4	2013-03-10	2015-12-12	\N	4	creado	200	25	\N	1
7	Proyecto 2	2014-05-12	2015-12-12	\N	6	activo	3000	10	2990	2
10	Proyecto con fases	2014-05-12	2014-06-05	2014-06-07	3	finalizado	3000	-200	2150	1
8	Proyecto 3	2013-03-10	2015-12-12	2014-06-07	3	finalizado	5000	0	4900	1
\.


--
-- Data for Name: fases_fases; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY fases_fases (id, nombre, "fechaInicioP", "fechaInicioR", estado, proyecto_id, costo, presupuesto, orden) FROM stdin;
29	Fase 1	2013-03-10	\N	finalizada	8	100	0	1
30	Fase 2	2013-03-10	\N	finalizada	8	0	0	2
31	Fase 3	2013-03-10	\N	finalizada	8	0	0	3
19	Fase 1	2014-05-12	\N	finalizada	6	30	0	1
20	Fase 2	2014-05-12	\N	finalizada	6	120	0	2
21	Fase 3	2014-05-12	\N	finalizada	6	10	0	3
22	Fase 4	2014-05-12	2014-06-07	finalizada	6	0	0	4
32	Fase 1	2013-03-10	\N	creado	9	120	0	1
33	Fase 2	2013-03-10	\N	creado	9	0	0	2
34	Fase 3	2013-03-10	\N	creado	9	0	0	3
35	Fase 4	2013-03-10	\N	creado	9	0	0	4
39	Fase 1	2013-03-10	2014-06-21	creado	11	0	0	1
40	Fase 2	2013-03-10	\N	creado	11	0	0	2
41	Fase 3	2013-03-10	\N	creado	11	0	0	3
42	Fase 4	2013-03-10	\N	creado	11	0	0	4
23	Fase 1	2014-05-12	\N	creado	7	20	0	1
24	Fase 2	2014-05-12	\N	creado	7	0	0	2
25	Fase 3	2014-05-12	\N	creado	7	0	0	3
26	Fase 4	2014-05-12	\N	creado	7	0	0	4
27	Fase 5	2014-05-12	\N	creado	7	0	0	5
28	Fase 6	2014-05-12	\N	creado	7	0	0	6
36	Fase 1	2014-05-12	2014-06-07	finalizada	10	250	0	1
37	Fase 2	2014-05-12	2014-06-07	finalizada	10	400	0	2
38	Fase 3	2014-05-12	2014-06-07	finalizada	10	0	0	3
\.


--
-- Name: fases_fases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('fases_fases_id_seq', 42, true);


--
-- Data for Name: items_items; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_items (id, nombre, "versionAct", estado, complejidad, fase_id, costo) FROM stdin;
15	Item 2	2	finalizado	1	19	10
18	Item 5	1	finalizado	3	21	10
25	Item nuevo	1	creado	1	32	100
27	Item 3	1	creado	15	32	10
26	Item 2	2	creado	15	32	10
14	Item 1	2	finalizado	1	19	10
17	Item 4	9	revision	1	20	10
28	Items 1	2	eliminado	1	23	10
29	Atributo 1	1	finalizado	15	23	10
16	Item 3	1	finalizado	1	19	10
20	Item bucle	1	eliminado	15	20	100
19	otro item	1	finalizado	15	20	10
21	Atributo 1	1	finalizado	15	29	100
22	f1	1	finalizado	15	36	100
23	hola	1	finalizado	3	36	150
24	Atributo 1	1	finalizado	10	37	400
\.


--
-- Data for Name: items_atributo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_atributo (id, nombre, descripcion, version, item_id) FROM stdin;
1	Atributo 1	aaaaaaaaaaa	2	17
2	Atributo 1	aaaaaaaaaaa	3	17
3	Atributo 2	bbbbbbbbb	3	17
4	Atributo 1	aaaaaaaaaaa	4	17
5	Atributo 2	bbbbbbbbb	4	17
6	atributo 3	cccccccccc	4	17
7	Atributo 1	aaaaaaaaaaa	5	17
8	Atributo 2	bbbbbbbbb	5	17
9	atributo 3	cccccccccc	5	17
10	Atributo 1	aaaaaaaaaaa	6	17
11	Atributo 2	bbbbbbbbb	6	17
12	atributo 3	cccccccccc	6	17
13	Atributo 5	dddddddd	6	17
14	Atributo 1	aaaaaaaaaaa	7	17
15	Atributo 2	bbbbbbbbb	7	17
16	atributo 3	cccccccccc	7	17
17	Atributo 1	aaaaaaaaaaa	8	17
18	Atributo 2	bbbbbbbbb	8	17
19	atributo 3	cccccccccc	8	17
20	Atributo despues de revision	aaaaaaa	8	17
21	hola	aaaaaaaaaaa	2	15
22	Atributo 1	Necesito Cambiar	2	26
23	Atributo 1	aaaaaaaaaaa	9	17
24	Atributo 2	bbbbbbbbb	9	17
25	atributo 3	cccccccccc	9	17
26	Atributo despues de revision	aaaaaaa	9	17
27	Atributo 1	aaaaaaaaaaa	2	28
\.


--
-- Name: items_atributo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_atributo_id_seq', 27, true);


--
-- Name: items_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_items_id_seq', 29, true);


--
-- Data for Name: items_relacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_relacion (id, "itemHijo_id", "itemPadre_id", estado) FROM stdin;
10	16	14	t
13	19	15	t
14	18	19	t
11	17	15	t
15	20	19	f
16	23	22	t
17	24	22	t
20	27	25	t
18	26	25	t
\.


--
-- Name: items_relacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_relacion_id_seq', 20, true);


--
-- Data for Name: items_tipoitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY items_tipoitem (id, nombre, atributos) FROM stdin;
5	Requerimiento Funcional	(lp0\n.
\.


--
-- Name: items_tipoitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('items_tipoitem_id_seq', 5, true);


--
-- Data for Name: lineasBase_lineasbase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "lineasBase_lineasbase" (id, nombre, estado, fase_id) FROM stdin;
12	L4	cerrado	19
13	Atributo 1	cerrado	36
14	Item Importado	cerrado	37
10	L1	abierto	19
11	L3	abierto	20
\.


--
-- Name: lineasBase_lineasbase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineasBase_lineasbase_id_seq"', 14, true);


--
-- Data for Name: lineasBase_relacionitemlineabase; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "lineasBase_relacionitemlineabase" (id, item_id, linea_id) FROM stdin;
11	14	10
12	15	10
13	17	11
14	16	12
15	22	13
16	23	13
17	24	14
\.


--
-- Name: lineasBase_relacionitemlineabase_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"lineasBase_relacionitemlineabase_id_seq"', 17, true);


--
-- Data for Name: permisos_permisos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY permisos_permisos (id, permiso, "tipoObjeto", usuario_id, grupo_id, id_fk) FROM stdin;
90	ADDI	proyecto	1	\N	7
91	FINI	proyecto	1	\N	7
94	REVI	proyecto	2	\N	7
95	GRAF	proyecto	2	\N	7
96	DELI	proyecto	2	\N	7
97	MODI	proyecto	2	\N	7
98	ADMINLIDER	permiso	3	\N	0
99	ADMINDEL	permiso	3	\N	0
100	ADMINDEL	permiso	\N	1	0
102	ADMINADD	permiso	\N	1	0
103	ADMINLIDER	permiso	1	\N	0
6	VER	proyecto	\N	\N	0
7	ADD	proyecto	1	\N	0
8	VER	proyecto	1	\N	0
9	VER	proyecto	2	\N	0
10	ADD	proyecto	2	\N	0
11	VER	proyecto	3	\N	0
15	CLB	proyecto	2	\N	10
16	LLB	proyecto	2	\N	10
17	GRAF	proyecto	2	\N	10
27	CLB	proyecto	1	\N	6
28	LLB	proyecto	1	\N	6
29	REVI	proyecto	1	\N	6
30	VERR	proyecto	1	\N	6
\.


--
-- Name: permisos_permisos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('permisos_permisos_id_seq', 104, true);


--
-- Data for Name: proyectos_miembros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proyectos_miembros (id, proyecto_id, miembro_id, comite) FROM stdin;
3	6	1	t
4	9	3	f
5	10	2	f
6	7	2	f
7	7	1	f
\.


--
-- Name: proyectos_miembros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_miembros_id_seq', 7, true);


--
-- Name: proyectos_proyectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proyectos_proyectos_id_seq', 11, true);


--
-- Data for Name: solicitudCambio_solicitudcambio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "solicitudCambio_solicitudcambio" (id, descripcion, "fechaExpiracion", "lineaBase_id", item_id, "costoAdicional", estado, orden, usuario_id) FROM stdin;
9	Necesito Cambiar	2014-05-13	11	17	1000	expirado	4	2
10	De vuelta voy a cambiar	2014-06-13	11	17	100	ejecutado	7	1
11	Otra solicitud	2014-06-13	11	17	100	ejecutado	7	2
13	Necesito Cambiar	2014-06-14	10	15	100	ejecutado	1	1
12	Necesito Cambiar	\N	10	14	100	rechazada	1	1
8	Necesito Cambiar	2014-06-13	10	14	100	expirado	1	1
14	Iteracion	2014-06-14	11	17	100	expirado	8	1
\.


--
-- Name: solicitudCambio_solicitudcambio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_solicitudcambio_id_seq"', 14, true);


--
-- Data for Name: solicitudCambio_votos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY "solicitudCambio_votos" (id, solicitud_id, estado, usuario_id, aceptar) FROM stdin;
13	8	listo	1	t
14	8	listo	2	t
16	9	listo	2	t
15	9	listo	1	t
17	10	listo	1	t
18	10	listo	2	t
20	11	listo	2	t
19	11	listo	1	t
23	13	listo	1	t
24	13	listo	2	t
21	12	listo	1	f
22	12	listo	2	f
25	14	listo	1	t
26	14	listo	2	t
\.


--
-- Name: solicitudCambio_votos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('"solicitudCambio_votos_id_seq"', 26, true);


--
-- PostgreSQL database dump complete
--

