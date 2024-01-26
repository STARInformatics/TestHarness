"""Example tests for the Test Harness."""
from translator_testing_model.datamodel.pydanticmodel import TestSuite

example_test_cases = TestSuite.parse_obj(
    {
        "id": "TestSuite_1",
        "name": None,
        "description": None,
        "tags": [],
        "test_metadata": {
            "id": "1",
            "name": None,
            "description": None,
            "tags": [],
            "test_source": "SMURF",
            "test_reference": None,
            "test_objective": "AcceptanceTest",
            "test_annotations": [],
        },
        "test_cases": {
            "TestCase_1": {
                "id": "TestCase_1",
                "name": "what treats MONDO:0010794",
                "description": "Valproic_Acid_treats_NARP_Syndrome; Barbiturates_treats_NARP_Syndrome",
                "tags": [],
                "test_env": "ci",
                "query_type": None,
                "test_assets": [
                    {
                        "id": "Asset_3",
                        "name": "Valproic_Acid_treats_NARP_Syndrome",
                        "description": "Valproic_Acid_treats_NARP_Syndrome",
                        "tags": [],
                        "input_id": "MONDO:0010794",
                        "input_name": "NARP Syndrome",
                        "input_category": None,
                        "predicate_id": "biolink:treats",
                        "predicate_name": "treats",
                        "output_id": "DRUGBANK:DB00313",
                        "output_name": "Valproic Acid",
                        "output_category": None,
                        "association": None,
                        "qualifiers": [],
                        "expected_output": "NeverShow",
                        "test_issue": None,
                        "semantic_severity": None,
                        "in_v1": None,
                        "well_known": False,
                        "test_reference": None,
                        "runner_settings": ["inferred"],
                        "test_metadata": {
                            "id": "1",
                            "name": None,
                            "description": None,
                            "tags": [],
                            "test_source": "SMURF",
                            "test_reference": "https://github.com/NCATSTranslator/Feedback/issues/147",
                            "test_objective": "AcceptanceTest",
                            "test_annotations": [],
                        },
                    },
                    {
                        "id": "Asset_4",
                        "name": "Barbiturates_treats_NARP_Syndrome",
                        "description": "Barbiturates_treats_NARP_Syndrome",
                        "tags": [],
                        "input_id": "MONDO:0010794",
                        "input_name": "NARP Syndrome",
                        "input_category": None,
                        "predicate_id": "biolink:treats",
                        "predicate_name": "treats",
                        "output_id": "MESH:D001463",
                        "output_name": "Barbiturates",
                        "output_category": None,
                        "association": None,
                        "qualifiers": [],
                        "expected_output": "NeverShow",
                        "test_issue": None,
                        "semantic_severity": None,
                        "in_v1": None,
                        "well_known": False,
                        "test_reference": None,
                        "runner_settings": ["inferred"],
                        "test_metadata": {
                            "id": "1",
                            "name": None,
                            "description": None,
                            "tags": [],
                            "test_source": "SMURF",
                            "test_reference": "https://github.com/NCATSTranslator/Feedback/issues/147",
                            "test_objective": "AcceptanceTest",
                            "test_annotations": [],
                        },
                    },
                ],
                "preconditions": [],
                "trapi_template": None,
                "components": ["ars"],
                "test_case_objective": "AcceptanceTest",
                "test_case_source": None,
                "test_case_predicate_name": "treats",
                "test_case_predicate_id": "biolink:treats",
                "test_case_input_id": "MONDO:0010794",
                "test_case_runner_settings": ["inferred"],
            }
        },
    }
).test_cases
