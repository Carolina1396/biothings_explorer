API_LIST = [
    "mygene",
    "ctd",
    "cord_gene",
    "cord_protein",
    "cord_chemical",
    "cord_disease",
    "cord_cell",
    "cord_molecular_activity",
    "cord_biological_process",
    "cord_cellular_component",
    "cord_anatomy",
    "cord_genomic_entity",
    "semmed_gene",
    "semmed_chemical",
    "semmed_disease",
    "semmed_biological_process",
    "semmed_anatomy",
    "semmed_phenotype",
    "scibite",
    "biolink",
    "opentarget",
    "dgidb",
    "mydisease",
    "mychem",
    "myvariant",
    "DISEASES",
    "scigraph",
    "pharos",
    "hmdb",
    "hetio",
    "chembio",
    "mgi_gene2phenotype",
    "ebi_gene2phenotype",
    "quickgo",
    "litvar",
    "ontology_lookup_service",
]

ID_RESOLVING_APIS = {
    "Gene": {
        "id_ranks": [
            "NCBIGene",
            "ENSEMBL",
            "HGNC",
            "UMLS",
            "UNIPROTKB",
            "SYMBOL",
            "OMIM",
            "MGI",
        ],
        "semantic": "Gene",
        "api_name": "mygene.info",
        "url": "https://mygene.info/v3",
        "mapping": {
            "NCBIGene": ["entrezgene"],
            "name": ["name"],
            "SYMBOL": ["symbol"],
            "UMLS": ["umls.cui", "umls.protein_cui"],
            "HGNC": ["HGNC"],
            "UNIPROTKB": ["uniprot.Swiss-Prot"],
            "ENSEMBL": ["ensembl.gene"],
            "OMIM": ["OMIM"],
            "MGI": ["MGI"],
        },
    },
    "SequenceVariant": {
        "id_ranks": ["DBSNP", "MYVARIANT_HG19", "HGVS", "ClinVar"],
        "api_name": "myvariant.info",
        "semantic": "SequenceVariant",
        "url": "https://myvariant.info/v1",
        "mapping": {
            "DBSNP": ["dbsnp.rsid", "clinvar.rsid", "dbnsfp.rsid"],
            "HGVS": [
                "clinvar.hgvs.genomic",
                "clinvar.hgvs.protein",
                "clinvar.hgvs.coding",
            ],
            "ClinVar": ["clinvar.rcv.accession"],
            "name": ["dbsnp.rsid", "clinvar.rsid", "dbnsfp.rsid"],
        },
    },
    "ChemicalSubstance": {
        "id_ranks": [
            "CHEBI",
            "CHEMBL.COMPOUND",
            "DRUGBANK",
            "PUBCHEM",
            "MESH",
            "UNII",
            "UMLS",
            "name",
            "CAS",
            "IUPAC",
            "formula",
        ],
        "semantic": "ChemicalSubstance",
        "api_name": "mychem.info",
        "url": "https://mychem.info/v1",
        "mapping": {
            "CHEMBL.COMPOUND": [
                "chembl.molecule_chembl_id",
                "drugbank.xrefs.chembl",
                "drugcentral.xrefs.chembl_id",
            ],
            "DRUGBANK": [
                "drugcentral.xrefs.drugbank_id",
                "pharmgkb.xrefs.drugbank",
                "chebi.xrefs.drugbank",
                "drugbank.id",
            ],
            "PUBCHEM": [
                "pubchem.cid",
                "drugbank.xrefs.pubchem.cid",
                "drugcentral.xrefs.pubchem_cid",
                "pharmgkb.xrefs.pubchem.cid",
            ],
            "CHEBI": [
                "chebi.id",
                "chembl.chebi_par_id",
                "drugbank.xrefs.chebi",
                "drugcentral.xrefs.chebi",
            ],
            "UMLS": ["drugcentral.xrefs.umlscui", "pharmgkb.xrefs.umls", "umls.cui"],
            "MESH": [
                "umls.mesh",
                "drugcentral.xrefs.mesh_descriptor_ui",
                "ginas.xrefs.MESH",
                "pharmgkb.xrefs.mesh",
            ],
            "UNII": [
                "drugcentral.xrefs.unii",
                "unii.unii",
                "aeolus.unii",
                "ginas.unii",
            ],
            "INCHIKEY": [
                "drugbank.inchi_key",
                "ginas.inchikey",
                "unii.inchikey",
                "chebi.inchikey",
            ],
            "INCHI": ["drugbank.inchi", "chebi.inchi", "chembl.inchi"],
            "KEGG": ["drugbank.xrefs.kegg.cid"],
            "name": [
                "chembl.pref_name",
                "drugbank.name",
                "umls.name",
                "ginas.preferred_name",
                "pharmgkb.name",
                "chebi.name",
                "drugbank.international_brands.name",
                "chembl.molecule_synonyms.synonyms",
                "drugbank.synonyms",
                "drugcentral.synonyms",
                "chebi.synonyms",
            ],
            "CAS": ["ginas.cas_primary", "pharmgkb.xrefs.cas", "chebi.xrefs.cas"],
            "IUPAC": ["pubchem.iupac.traditional", "drugbank.iupac"],
            "formula": [
                "chebi.formulae",
                "drugbank.formula",
                "pubchem.molecular_formula",
            ],
        },
    },
    "Disease": {
        "id_ranks": ["MONDO", "DOID", "OMIM", "ORPHANET", "UMLS", "MESH", "name"],
        "semantic": "Disease",
        "api_name": "mydisease.info",
        "url": "http://mydisease.info/v1",
        "mapping": {
            "MONDO": ["mondo.mondo"],
            "DOID": ["mondo.xrefs.doid"],
            "UMLS": ["mondo.xrefs.umls", "disgenet.xrefs.umls"],
            "name": [
                "mondo.label",
                "disgenet.xrefs.disease_name",
                "mondo.synonyms.exact",
                "mondo.synonyms.related",
                "disease_ontology.synonyms.exact",
            ],
            "MESH": ["mondo.xrefs.mesh", "disease_ontology.xrefs.mesh", "ctd.mesh"],
            "OMIM": ["mondo.xrefs.omim", "hpo.omim"],
            "ORPHANET": ["hpo.orphanet", "mondo.xrefs.orphanet"],
        },
    },
    "PhenotypicFeature": {
        "id_ranks": [
            "UMLS",
            "SNOMEDCT",
            "HP",
            "MEDDRA",
            "EFO",
            "NCIT",
            "MESH",
            "MP",
            "name",
        ],
        "semantic": "PhenotypicFeature",
        "api_name": "HPO API",
        "url": "https://biothings.ncats.io/hpo",
        "mapping": {
            "UMLS": ["xrefs.umls"],
            "SNOMEDCT": ["xrefs.snomed_ct"],
            "HP": ["hp"],
            "MEDDRA": ["xrefs.meddra"],
            "EFO": ["xrefs.efo"],
            "NCIT": ["xrefs.ncit"],
            "MESH": ["xrefs.mesh"],
            "MP": ["xrefs.mp"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
    "MolecularActivity": {
        "id_ranks": ["GO", "MetaCyc", "RHEA", "KEGG", "REACT", "name"],
        "semantic": "MolecularActivity",
        "api_name": "Gene Ontology Molecular Function API",
        "url": "https://biothings.ncats.io/go_mf",
        "mapping": {
            "GO": ["go"],
            "MetaCyc": ["xrefs.metacyc"],
            "RHEA": ["xrefs.rhea"],
            "KEGG": ["xrefs.kegg_reaction"],
            "REACT": ["xrefs.reactome"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
    "BiologicalProcess": {
        "id_ranks": ["GO", "MetaCyc", "REACT", "KEGG", "name"],
        "semantic": "BiologicalProcess",
        "api_name": "Gene Ontology Biological Process API",
        "url": "https://biothings.ncats.io/go_bp",
        "mapping": {
            "GO": ["go"],
            "MetaCyc": ["xrefs.metacyc"],
            "KEGG": ["xrefs.kegg_pathway"],
            "REACT": ["xrefs.reactome"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
    "CellularComponent": {
        "id_ranks": ["GO", "MetaCyc", "RHEA", "name"],
        "semantic": "CellularComponent",
        "api_name": "Gene Ontology Cellular Component API",
        "url": "https://biothings.ncats.io/go_cc",
        "mapping": {
            "GO": ["go"],
            "MetaCyc": ["xrefs.metacyc"],
            "RHEA": ["xrefs.rhea"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
    "Pathway": {
        "id_ranks": ["REACT", "KEGG", "PHARMGKB", "WIKIPATHWAYS", "name"],
        "semantic": "Pathway",
        "api_name": "geneset API",
        "url": "https://biothings.ncats.io/geneset",
        "mapping": {
            "REACT": ["reactome"],
            "WIKIPATHWAYS": ["wikipathways"],
            "KEGG": ["kegg"],
            "PHARMGKB": ["pharmgkb"],
            "name": ["name"],
        },
    },
    "AnatomicalEntity": {
        "id_ranks": ["UBERON", "UMLS", "MESH", "NCIT", "name"],
        "semantic": "AnatomicalEntity",
        "api_name": "UBERON API",
        "url": "https://biothings.ncats.io/uberon",
        "mapping": {
            "UBERON": ["uberon"],
            "UMLS": ["xrefs.umls"],
            "MESH": ["xrefs.mesh"],
            "NCIT": ["xrefs.ncit"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
    "Cell": {
        "id_ranks": ["CL", "NCIT", "MESH", "EFO", "name"],
        "semantic": "Cell",
        "api_name": "Cell Ontology API",
        "url": "https://biothings.ncats.io/cell_ontology",
        "mapping": {
            "CL": ["cl"],
            "NCIT": ["xrefs.ncit"],
            "MESH": ["xrefs.mesh"],
            "EFO": ["xrefs.efo"],
            "name": ["name", "synonym.exact", "synonym.related", "synonym.broad"],
        },
    },
}

MAX_CONCURRENT_QUERIES_ON_SINGLE_API = 5

ALWAYS_PREFIXED = [
    "RHEA",
    "GO",
    "CHEBI",
    "HP",
    "MONDO",
    "DOID",
    "EFO",
    "UBERON",
    "MP",
    "CL",
    "MGI",
]

SEMANTIC_TYPES_TO_EXPAND = [
    "Disease",
    "PhenotypicFeature",
    "AnatomicalEntity",
    "BiologicalProcess",
    "CellularComponent",
    "MolecularActivity",
]

EXPAND_API_LIST = [
    "mydisease.info API",
    "Gene Ontology Cellular Component API",
    "Gene Ontology Biological Process API",
    "UBERON Ontology API",
    "Gene Ontology Molecular Activity API",
    "Human Phenotype Ontology API",
]

BTE_FILTERS = ["nodeDegree", "ngd", "drugPhase", "survivalProbability"]
