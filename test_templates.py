import unittest
import os
import re

class TestTemplates(unittest.TestCase):
    def test_result_template_structure(self):
        self.assertTrue(os.path.exists("RESULT-TEMPLATE.md"))
        with open("RESULT-TEMPLATE.md", "r", encoding="utf-8") as f:
            content = f.read()

        required_fields = [
            "- 日期：",
            "- 成果標題：",
            "- 我想幫助的人與問題：",
            "- 本輪可投入的時間：",
            "- 完成條件：",
            "- 我做了什麼：",
            "- 可公開的成果連結：",
            "- 回饋與下一步："
        ]

        for field in required_fields:
            self.assertIn(field, content, f"Missing required field in RESULT-TEMPLATE.md: {field}")

        self.assertIn("# 本輪成果", content, "Missing title in RESULT-TEMPLATE.md")

    def test_skill_md_structure(self):
        self.assertTrue(os.path.exists("SKILL.md"))
        with open("SKILL.md", "r", encoding="utf-8") as f:
            content = f.read()

        required_headers = [
            "# 需求訪談與合作提案",
            "## 找出問題與受益者",
            "## 盤點投入與範圍",
            "## 提出最小試作",
            "## 確認下一步",
            "## 完成時交付"
        ]

        for header in required_headers:
            self.assertIn(header, content, f"Missing required header in SKILL.md: {header}")

        # Check frontmatter exists
        self.assertTrue(content.startswith("---"), "SKILL.md does not start with frontmatter")
        self.assertIn("name: freedom-skill-partnership", content)
        self.assertIn("description:", content)

    def test_no_hardcoded_secrets_in_templates(self):
        """Test that static template files do not contain exposed hardcoded secrets."""
        files_to_check = ["RESULT-TEMPLATE.md", "SKILL.md", "skill-book.json"]

        # simple check for common secret variable names with assignments
        secret_patterns = [
            r"password\s*=\s*['\"][^'\"]+['\"]",
            r"api_key\s*=\s*['\"][^'\"]+['\"]",
            r"secret\s*=\s*['\"][^'\"]+['\"]",
            r"token\s*=\s*['\"][^'\"]+['\"]"
        ]

        for filepath in files_to_check:
            self.assertTrue(os.path.exists(filepath), f"{filepath} does not exist")
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            for pattern in secret_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                self.assertEqual(len(matches), 0, f"Found potential exposed secret matching {pattern} in {filepath}")

if __name__ == "__main__":
    unittest.main()
