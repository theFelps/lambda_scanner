def create_type_0():
    query = """create table type_0 ( 
	id int not null auto_increment ,
	tipo_registro int , 
	num_sequencia int , 
	data_geracao_arquivo int ,
	operadora varchar(255) ,
	uf_operadora varchar(255) ,
	codigo_cliente int ,
	nome_cliente varchar(255) ,
	cgc_cliente varchar(255) ,
	id_conta_unica int ,
	data_vencimento int ,
	data_emissao int ,
	primary key (id), 
	unique (id_conta_unica)) 

	engine = innodb;"""
    return query

def create_type_1():
    query = """create table type_1 (
    id int not null auto_increment,
    tipo_registro  int not null,
    num_sequencia int,
    id_conta_unica varchar(25),
    data_vencimento int,
    data_emissao int,
    id_unico_recurso varchar(25),
    cnl_recurso int,
    nome_localidade varchar(255),
    ddd varchar(2),
    n_telefone varchar(10),
    tipo_servico varchar(4),
    desc_tipo_servico varchar(35),
    caracteristica_recurso varchar(15),
    degrau_recurso varchar(2),
    velocidade_recurso varchar(5),
    unidade_velocidade_recurso varchar(4),
    inicio_periodo_assinatura int,
    fim_periodo_assinatura int,
    inicio_periodo_servico int,
    fim_periodo_servico int,
    unidade_consumo varchar(5),
    quantidade_consumo int,
    sinal_valor_consumo varchar(2),
    valor_consumo int,
    sinal_assinatura varchar(2),
    valor_assinatura int,
    aliquota varchar(3),
    sinal_icms varchar(1),
    valor_icms int,
    sinal_total_outros_impostos varchar(1),
    valor_total_outros_impostos int,
    numero_nota_fiscal varchar(12),
    sinal_valor_conta varchar(1),
    valor_conta int,
    PRIMARY KEY(id))
    engine = innodb;"""
    return query

def create_type_2():
	query = """create table type_2 (
	tipo_registro int,
	num_sequencia int,
	id_unico_recurso varchar(25),
	ddd varchar(2),
	numero_telefone varchar(10),
	caracteristica_recurso varchar(15),
	cnl_recurso_a varchar(5),
	localidade_a varchar(20),
	uf_a varchar(2),
	endereco_a varchar(30),
	numero_endereco_a varchar(5),
	complemento_a varchar(10),
	bairro_a varchar(20),
	cnl_recurso_b varchar(5),
	localidade_b varchar(20),
	uf_b varchar(2),
	endereco_b varchar(30),
	numero_endereco_b varchar(5),
	complemento_b varchar(10),
	bairro_b varchar(20))
	engine = innodb;"""
	return query

def create_type_3():
	query = """create table type_3 (
	tipo_registro varchar(1),
	num_sequencia int,
	data_vencimento int,
	data_emissao int,
	identificador_unico_recurso varchar(25),
	cnl_recurso int,
	ddd varchar(2),
	numero_telefone varchar(2),
	caracteristica_recurso varchar(15),
	degrau_recurso varchar(2),
	data_ligacao int,
	cnl_localidade_chamada int,
	nome_localidade_chamada varchar(25),
	uf_telefone_chamado varchar(2),
	codigo_nacional_internacional varchar(2),
	codigo_operadora varchar(2),
	descricao_operadora varchar(255),
	codigo_pais_chamado varchar(3),
	area_ddd varchar(4),
	numero_telefone_chamado varchar(10),
	conjugado_numero_telefone_chamado varchar(2),
	duracao_ligacao int,
	categoria varchar(3),
	descricao_categoria varchar(50),
	horario_ligacao varchar(6),
	tipo_chamada varchar(1),
	grupo_horario_tarifario varchar(10),
	descricao_horario_tarifario varchar(25),
	degrau_ligacao varchar(2),
	sinal_valor_ligacao varchar(1),
	aliquota_icms varchar(5),
	valor_ligacao_com_imposto varchar(13),
	classe_servico int)
	engine = innodb;"""
	return query

def create_type_4():
	query="""create table type_4 (
	tipo_registro int,
	num_sequencia int,
	data_vencimento int,
	data_emissao int,
	identificador_unico_recurso varchar(25),
	cnl_recurso int,
	ddd varchar(2),
	numero_telefone varchar(10),
	caracteristica_recurso varchar(15),
	data_servico int,
	cnl_localidade_chamada int,
	nome_localidade_chamada varchar(25),
	uf_telefone_chamado varchar(2),
	codigo_nacional_internacional varchar(2),
	codigo_operadora varchar(2),
	descricao_operadora varchar(20),
	codigo_pais_chamado varchar(3),
	area_ddd varchar(4),
	numero_telefone_chamado varchar(10),
	conjugado_numero_telefone_chamado varchar(2),
	duracao_ligacao int,
	horario_ligacao varchar(6),
	grupo_categoria varchar(3),
	descricao_grupo_categoria varchar(30),
	categoria varchar(3),
	descricao_categoria varchar(40),
	sinal_valor_ligacao varchar(1),
	valor_ligacao int,
	classe_servico int
	)
	engine = innodb;"""
	return query

def create_type_5():
	query="""CREATE TABLE type_5 (
	tipo_registro INT,
	num_sequencia INT,
	data_vencimento INT,
	data_emissao INT,
	identificador_unico_recurso VARCHAR(25),
	identificador_conta_unica VARCHAR(25),
	cnl_recurso INT,
	ddd VARCHAR(2),
	numero_telefone VARCHAR(10),
	grupo_categoria VARCHAR(3),
	descricao_grupo_categoria VARCHAR(80),
	sinal_valor_ligacao VARCHAR(1),
	base_calculo_desconto INT,
	percentual_desconto INT,
	valor_ligacao INT,
	data_inicio_acerto INT,
	hora_inicio_acerto INT,
	data_fim_acerto INT,
	hora_fim_acerto INT,
	classe_servico INT)
	ENGINE = InnoDB;"""
	return query

def create_type_9():
	query="""CREATE TABLE type_9 (
	tipo_registro INT,
	num_sequencia INT,
	codigo_cliente VARCHAR(15),
	identificacao_conta_unica VARCHAR(25),
	data_vencimento INT,
	data_emissao INT,
	quantidade_registros INT,
	quantidade_linhas INT,
	sinal_total VARCHAR(1),
	valor_total INT
	)
	ENGINE = InnoDB;"""
	return query
