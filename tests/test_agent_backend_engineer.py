"""Tests for the backend-engineer agent.

This module tests the backend-engineer agent definition files to ensure:
- Files exist in the correct locations
- YAML frontmatter is valid and complete
- Required tools are configured
- Agent description matches its purpose
- Content includes necessary sections and standards
"""

import re
from pathlib import Path
from typing import Dict

import pytest


def _read_agent_file_safe(file_path: Path) -> str:
    """Safely read agent file with proper encoding.

    Args:
        file_path: Path to the agent file to read

    Returns:
        str: Contents of the file

    Raises:
        pytest.skip: If file doesn't exist (for graceful test skipping)
        FileNotFoundError: If file not found (for assertion failures)
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Agent file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def _parse_frontmatter(content: str) -> Dict[str, str]:
    """Extract and parse YAML frontmatter from agent content.

    Args:
        content: Full content of the agent file

    Returns:
        Dict[str, str]: Parsed frontmatter as key-value pairs

    Raises:
        pytest.fail: If no valid frontmatter found
    """
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        pytest.fail("No YAML frontmatter found in agent file")

    # Parse frontmatter manually since description contains colons
    frontmatter_text = match.group(1)
    result: Dict[str, str] = {}

    for line in frontmatter_text.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()

    return result


@pytest.fixture
def agent_file_path() -> Path:
    """Return path to backend-engineer agent file.

    Returns:
        Path: Path to .claude/agents/backend-engineer.md
    """
    return Path(".claude/agents/backend-engineer.md")


@pytest.fixture
def template_file_path() -> Path:
    """Return path to backend-engineer template file.

    Returns:
        Path: Path to templates/agents/backend-engineer.md
    """
    return Path("templates/agents/backend-engineer.md")


@pytest.fixture
def agent_content(agent_file_path: Path) -> str:
    """Return content of the backend-engineer agent file.

    Args:
        agent_file_path: Path to the agent file

    Returns:
        str: Full content of the agent file with UTF-8 encoding
    """
    return _read_agent_file_safe(agent_file_path)


@pytest.fixture
def frontmatter(agent_content: str) -> Dict[str, str]:
    """Extract and parse YAML frontmatter from agent content.

    Args:
        agent_content: Full content of the agent file

    Returns:
        Dict[str, str]: Parsed frontmatter key-value pairs
    """
    return _parse_frontmatter(agent_content)


class TestBackendEngineerAgentFile:
    """Test the backend-engineer agent file exists and is valid."""

    def test_agent_file_exists(self, agent_file_path: Path) -> None:
        """Agent file should exist in .claude/agents/.

        Args:
            agent_file_path: Path to the agent file
        """
        assert agent_file_path.exists(), (
            f"Backend engineer agent file not found at {agent_file_path}. "
            "Expected location: .claude/agents/backend-engineer.md"
        )

    def test_template_file_exists(self, template_file_path: Path) -> None:
        """Template file should exist in templates/agents/.

        Args:
            template_file_path: Path to the template file
        """
        assert template_file_path.exists(), (
            f"Backend engineer template file not found at {template_file_path}. "
            "Expected location: templates/agents/backend-engineer.md"
        )

    def test_files_are_identical(
        self, agent_file_path: Path, template_file_path: Path
    ) -> None:
        """Agent file and template file should be identical.

        Args:
            agent_file_path: Path to the agent file
            template_file_path: Path to the template file
        """
        agent_content = _read_agent_file_safe(agent_file_path)
        template_content = _read_agent_file_safe(template_file_path)
        assert agent_content == template_content, (
            f"Agent file ({agent_file_path}) and template file ({template_file_path}) "
            "should be identical. The template is the authoritative source and should "
            "be copied to .claude/agents/ during project initialization."
        )


class TestBackendEngineerFrontmatter:
    """Test the YAML frontmatter of the backend-engineer agent."""

    def test_has_frontmatter(self, agent_content: str) -> None:
        """Agent file should have YAML frontmatter.

        Args:
            agent_content: Full content of the agent file
        """
        assert agent_content.startswith("---\n"), (
            "Agent file must start with YAML frontmatter delimiter '---\\n'. "
            "Frontmatter is required for Claude Code agent recognition."
        )
        assert "\n---\n" in agent_content, (
            "Agent file must have closing YAML frontmatter delimiter '\\n---\\n'. "
            "Missing closing delimiter indicates malformed frontmatter."
        )

    def test_frontmatter_is_valid(self, frontmatter: Dict[str, str]) -> None:
        """Frontmatter should be parseable as key-value pairs.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        assert isinstance(frontmatter, dict), (
            f"Frontmatter should be a dictionary, got {type(frontmatter).__name__}"
        )
        assert len(frontmatter) > 0, (
            "Frontmatter should have at least one field. Empty frontmatter is invalid."
        )

    def test_has_name_field(self, frontmatter: Dict[str, str]) -> None:
        """Frontmatter should have a name field.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        assert "name" in frontmatter, (
            "Frontmatter must have a 'name' field for agent identification"
        )
        assert frontmatter["name"] == "backend-engineer", (
            f"Agent name should be 'backend-engineer', got '{frontmatter.get('name')}'"
        )

    def test_has_description_field(self, frontmatter: Dict[str, str]) -> None:
        """Frontmatter should have a description field.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        assert "description" in frontmatter, (
            "Frontmatter must have a 'description' field explaining agent purpose"
        )
        description = frontmatter["description"]
        assert isinstance(description, str), (
            f"Description should be a string, got {type(description).__name__}"
        )
        assert len(description) > 50, (
            f"Description should be substantial (>50 chars), got {len(description)} chars"
        )

    def test_has_tools_field(self, frontmatter: Dict[str, str]) -> None:
        """Frontmatter should have a tools field.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        assert "tools" in frontmatter, (
            "Frontmatter must have a 'tools' field specifying available tools"
        )

    def test_has_color_field(self, frontmatter: Dict[str, str]) -> None:
        """Frontmatter should have a color field.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        assert "color" in frontmatter, (
            "Frontmatter should have a 'color' field for visual identification"
        )
        assert frontmatter["color"] == "green", (
            f"Backend engineer color should be 'green', got '{frontmatter.get('color')}'"
        )


class TestBackendEngineerTools:
    """Test the tools configuration for the backend-engineer agent."""

    def _get_tools_list(self, frontmatter: Dict[str, str]) -> list[str]:
        """Helper to extract tools list from frontmatter.

        Args:
            frontmatter: Parsed frontmatter dictionary

        Returns:
            list[str]: List of tool names
        """
        return frontmatter.get("tools", "").split(", ")

    def test_tools_list(self, frontmatter: Dict[str, str]) -> None:
        """Backend engineer should have appropriate tools.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        tools = self._get_tools_list(frontmatter)
        expected_tools = ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]

        assert len(tools) > 0, (
            "Agent should have tools configured. Tools are required for agent functionality."
        )

        for tool in expected_tools:
            assert tool in tools, (
                f"Backend engineer must have '{tool}' tool. "
                f"Available tools: {', '.join(tools)}"
            )

    def test_has_file_manipulation_tools(self, frontmatter: Dict[str, str]) -> None:
        """Backend engineer should have file manipulation tools.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        tools = self._get_tools_list(frontmatter)

        # Backend engineers need to read and write code
        assert "Read" in tools, (
            "Backend engineer needs 'Read' tool to examine existing code"
        )
        assert "Write" in tools, (
            "Backend engineer needs 'Write' tool to create new files"
        )
        assert "Edit" in tools, (
            "Backend engineer needs 'Edit' tool to modify existing code"
        )

    def test_has_code_search_tools(self, frontmatter: Dict[str, str]) -> None:
        """Backend engineer should have code search tools.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        tools = self._get_tools_list(frontmatter)

        # Backend engineers need to search codebases
        assert "Glob" in tools, (
            "Backend engineer needs 'Glob' tool to find files by pattern"
        )
        assert "Grep" in tools, (
            "Backend engineer needs 'Grep' tool to search code content"
        )

    def test_has_bash_tool(self, frontmatter: Dict[str, str]) -> None:
        """Backend engineer should have Bash tool for running commands.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        tools = self._get_tools_list(frontmatter)

        # Backend engineers need to run migrations, tests, servers
        assert "Bash" in tools, (
            "Backend engineer needs 'Bash' tool to run migrations, tests, and servers"
        )


class TestBackendEngineerDescription:
    """Test the description field matches the agent's purpose."""

    def test_description_mentions_backend(self, frontmatter: Dict[str, str]) -> None:
        """Description should mention backend development.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        description = frontmatter["description"].lower()
        assert "backend" in description, (
            "Description must mention 'backend' development to clarify agent purpose. "
            f"Current description: {frontmatter['description'][:100]}..."
        )

    def test_description_mentions_api(self, frontmatter: Dict[str, str]) -> None:
        """Description should mention API work.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        description = frontmatter["description"].lower()
        assert "api" in description, (
            "Description should mention 'API' work as a core backend responsibility. "
            f"Current description: {frontmatter['description'][:100]}..."
        )

    def test_description_mentions_database(self, frontmatter: Dict[str, str]) -> None:
        """Description should mention database work.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        description = frontmatter["description"].lower()
        assert "database" in description or "db" in description, (
            "Description should mention 'database' or 'db' work as a core backend skill. "
            f"Current description: {frontmatter['description'][:100]}..."
        )

    def test_description_mentions_python(self, frontmatter: Dict[str, str]) -> None:
        """Description should mention Python.

        Args:
            frontmatter: Parsed frontmatter dictionary
        """
        description = frontmatter["description"].lower()
        assert "python" in description, (
            "Description should mention 'Python' as the primary backend language. "
            f"Current description: {frontmatter['description'][:100]}..."
        )


class TestBackendEngineerContent:
    """Test the content of the backend-engineer agent."""

    def test_has_core_technologies_section(self, agent_content: str) -> None:
        """Agent should document core technologies.

        Args:
            agent_content: Full content of the agent file
        """
        assert "## Core Technologies" in agent_content, (
            "Agent must have '## Core Technologies' section documenting "
            "the tech stack and frameworks used for backend development"
        )

    def test_mentions_python(self, agent_content: str) -> None:
        """Agent should mention Python.

        Args:
            agent_content: Full content of the agent file
        """
        assert "Python" in agent_content, (
            "Agent must mention 'Python' as the primary backend language"
        )

    def test_mentions_fastapi_or_flask(self, agent_content: str) -> None:
        """Agent should mention FastAPI or Flask.

        Args:
            agent_content: Full content of the agent file
        """
        assert "FastAPI" in agent_content or "Flask" in agent_content, (
            "Agent should mention 'FastAPI' or 'Flask' as web frameworks. "
            "These are the standard Python backend frameworks."
        )

    def test_mentions_databases(self, agent_content: str) -> None:
        """Agent should mention databases.

        Args:
            agent_content: Full content of the agent file
        """
        assert "PostgreSQL" in agent_content or "SQLite" in agent_content, (
            "Agent should mention database systems like 'PostgreSQL' or 'SQLite'. "
            "Database knowledge is essential for backend engineering."
        )

    def test_has_implementation_standards(self, agent_content: str) -> None:
        """Agent should have implementation standards section.

        Args:
            agent_content: Full content of the agent file
        """
        assert "## Implementation Standards" in agent_content, (
            "Agent must have '## Implementation Standards' section defining "
            "coding patterns, best practices, and conventions"
        )

    def test_has_testing_approach(self, agent_content: str) -> None:
        """Agent should have testing approach section.

        Args:
            agent_content: Full content of the agent file
        """
        assert "## Testing Approach" in agent_content, (
            "Agent must have '## Testing Approach' section explaining "
            "unit tests, integration tests, and testing strategies"
        )

    def test_mentions_security(self, agent_content: str) -> None:
        """Agent should mention security.

        Args:
            agent_content: Full content of the agent file
        """
        content_lower = agent_content.lower()
        assert "security" in content_lower, (
            "Agent must mention 'security' best practices. Security is critical "
            "for backend development (SQL injection, XSS, authentication, etc.)"
        )

    def test_mentions_validation(self, agent_content: str) -> None:
        """Agent should mention input validation.

        Args:
            agent_content: Full content of the agent file
        """
        content_lower = agent_content.lower()
        assert "validation" in content_lower or "validate" in content_lower, (
            "Agent must mention input 'validation'. Validating user input "
            "is essential for security and data integrity."
        )

    def test_has_code_quality_checklist(self, agent_content: str) -> None:
        """Agent should have a code quality checklist.

        Args:
            agent_content: Full content of the agent file
        """
        assert (
            "## Code Quality Checklist" in agent_content
            or "Code Quality" in agent_content
        ), (
            "Agent should have a 'Code Quality Checklist' section providing "
            "a verification checklist before completing tasks"
        )

    def test_has_checkbox_items(self, agent_content: str) -> None:
        """Agent should have checkbox items for verification.

        Args:
            agent_content: Full content of the agent file
        """
        assert "- [ ]" in agent_content, (
            "Agent should have checkbox items '- [ ]' for task verification. "
            "Checklists help ensure all requirements are met."
        )

    def test_mentions_type_hints(self, agent_content: str) -> None:
        """Agent should mention Python type hints.

        Args:
            agent_content: Full content of the agent file
        """
        assert "type hint" in agent_content.lower() or "Type hints" in agent_content, (
            "Agent must mention 'type hints' as a Python best practice. "
            "Type hints improve code quality and enable static analysis."
        )
