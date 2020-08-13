import unittest
from biothings_explorer.hint import Hint


class TestHint(unittest.TestCase):
    def setUp(self):
        self.ht = Hint()

    def mygene_test(self, res):
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.get("Gene"))
        self.assertIsNotNone(res.get("Gene")[0])
        bioentity = res.get("Gene")[0]
        self.assertEqual(bioentity["NCBIGene"], "1017")
        self.assertEqual(bioentity["type"], "Gene")
        self.assertEqual(bioentity["primary"]["identifier"], "NCBIGene")
        self.assertEqual(bioentity["primary"]["value"], "1017")
        self.assertEqual(bioentity["SYMBOL"], "CDK2")

    def myvariant_test(self, res):
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.get("SequenceVariant"))
        self.assertIsNotNone(res.get("SequenceVariant")[0])
        bioentity = res.get("SequenceVariant")[0]
        self.assertEqual(bioentity["DBSNP"], "rs12190874")
        self.assertEqual(bioentity["type"], "SequenceVariant")
        self.assertEqual(bioentity["primary"]["identifier"], "DBSNP")
        self.assertEqual(bioentity["primary"]["value"], "rs12190874")

    def test_gene_NCBIGene_id_as_input(self):
        """Test the output of Hint query when providing gene NCBIGene id as input."""
        res = self.ht.query("1017")
        self.mygene_test(res)

    def test_gene_SYMBOL_as_input(self):
        """Test the output of Hint query when providing gene SYMBOL as input."""
        res = self.ht.query("CDK2")
        self.mygene_test(res)

    def test_gene_UMLS_id_as_input(self):
        """Test the output of Hint query when providing gene UMLS id as input."""
        res = self.ht.query("C1332823")
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.get("Gene"))
        self.assertIsNotNone(res.get("Gene")[0])
        bioentity = res.get("Gene")[0]
        self.assertEqual(bioentity["UMLS"], "C1332823")
        self.assertEqual(bioentity["type"], "Gene")
        self.assertEqual(bioentity["primary"]["identifier"], "NCBIGene")
        self.assertEqual(bioentity["primary"]["value"], "7852")
        self.assertEqual(bioentity["SYMBOL"], "CXCR4")

    def test_gene_hgnc_id_as_input(self):
        """Test the output of Hint query when providing gene hgnc id as input."""
        res = self.ht.query("1771")
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.get("Gene"))
        self.assertIsNotNone(res.get("Gene")[0])
        bioentity = [item for item in res.get("Gene") if item.get("HGNC") == "1771"][0]
        self.assertEqual(bioentity["type"], "Gene")
        self.assertEqual(bioentity["primary"]["identifier"], "NCBIGene")
        self.assertEqual(bioentity["primary"]["value"], "1017")

    def test_gene_uniprot_id_as_input(self):
        """Test the output of Hint query when providing gene uniprot id as input."""
        res = self.ht.query("P24941")
        self.mygene_test(res)

    def test_variant_rsid_as_input(self):
        """Test the output of Hint query when providing variant dbsnp id as input."""
        res = self.ht.query("rs12190874")
        self.myvariant_test(res)

    def test_variant_hgvs_as_input(self):
        """Test the output of Hint query when providing variant hgvs id as input."""
        res = self.ht.query("chr6:g.42454850G>A")
        self.myvariant_test(res)

    def test_chemical(self):
        """Test the output of Hint query when providing chemical drugbank ID as input."""
        res = self.ht.query("DB01926")
        bioentity = res.get("ChemicalSubstance")[0]
        self.assertIsNotNone(res)
        self.assertEqual(bioentity["name"], "Carboxymycobactin S")

    def test_resolving_by_synonyms(self):
        """Test the output of Hint query when providing disease synonyms"""
        res = self.ht.query("GIST")
        bioentity = res.get("Disease")
        ids = [item.get("MONDO") for item in bioentity]
        self.assertIsNotNone(res)
        self.assertIn("MONDO:0011719", ids)
