# Dev Essentials - Claude Code Plugin

A comprehensive collection of development tools for Claude Code, including code review, testing, debugging, security auditing, and optimization capabilities.

## Features

### Slash Commands

- **`/review`** - Comprehensive code review covering quality, security, performance, testing, and documentation
- **`/test-plan`** - Generate detailed test plans with unit, integration, and e2e test cases
- **`/docs`** - Create comprehensive API documentation with examples and usage instructions
- **`/optimize`** - Analyze code for performance optimization opportunities
- **`/refactor`** - Refactor code to improve quality, maintainability, and apply design patterns

### Specialized Agents

- **debugging-agent** - Expert at analyzing errors, identifying root causes, and providing fixes
- **test-writer** - Writes comprehensive test suites with high coverage
- **refactoring-agent** - Improves code quality while maintaining functionality
- **security-auditor** - Identifies vulnerabilities and enforces secure coding practices

### Guidelines

Includes development best practices for:
- Code quality and style
- Testing requirements
- Security standards
- Performance optimization
- Documentation
- Version control

## Installation

### From Local Directory

If testing locally:

```bash
cd /path/to/claude_plugin
claude /plugin marketplace add .
claude /plugin install dev-essentials
```

### From GitHub Repository

Once published to GitHub:

```bash
claude /plugin marketplace add androidyue/claude_code_plugin_example
claude /plugin install dev-essentials
```

## Usage

### Using Slash Commands

```bash
# Review current changes
/review

# Generate test plan for a feature
/test-plan src/auth/login.ts

# Create documentation
/docs src/api/users.ts

# Optimize code performance
/optimize src/database/queries.ts

# Refactor code for better quality
/refactor src/legacy/user-service.js
```

### Using Specialized Agents

Agents can be invoked through the Task tool or when Claude Code automatically selects them based on your request:

```bash
# Claude will use the appropriate agent when you ask:
"Debug the authentication error I'm seeing"
"Write tests for the user service"
"Refactor this code to be more maintainable"
"Audit the security of the payment processing code"
```

## Plugin Structure

```
claude-dev-essentials/
├── .claude-plugin/
│   ├── plugin.json           # Plugin manifest
│   └── marketplace.json      # Marketplace configuration
├── commands/                  # Slash commands
│   ├── review.md
│   ├── test-plan.md
│   ├── docs.md
│   ├── optimize.md
│   └── refactor.md
├── agents/                    # Specialized agents
│   ├── debugging-agent.json
│   ├── test-writer.json
│   ├── refactoring-agent.json
│   └── security-auditor.json
├── CLAUDE.md                  # Development guidelines
└── README.md
```

## Customization

You can customize this plugin for your needs:

1. **Edit slash commands**: Modify files in `commands/` to adjust prompts
2. **Customize agents**: Edit JSON files in `agents/` to change agent behavior
3. **Update guidelines**: Modify `CLAUDE.md` to match your team's standards
4. **Add new commands**: Create new `.md` files in `commands/`
5. **Add new agents**: Create new `.json` files in `agents/`

## Sharing Your Plugin

### Option 1: GitHub Repository

1. Create a new GitHub repository
2. Push your plugin files
3. Others can install with:
   ```bash
   /plugin marketplace add androidyue/claude_code_plugin_example
   /plugin install dev-essentials
   ```

### Option 2: Direct Distribution

Share the plugin directory directly. Users can add it as a local marketplace:

```bash
/plugin marketplace add /path/to/plugin
/plugin install dev-essentials
```

## Contributing

Feel free to customize and extend this plugin. Some ideas:

- Add more specialized agents (e.g., API design, database optimization)
- Create domain-specific slash commands
- Add hooks for automated workflows
- Integrate MCP servers for tool connectivity

## License

MIT

## Author

androidyue
- GitHub: [@androidyue](https://github.com/androidyue)
- Repository: [claude_code_plugin_example](https://github.com/androidyue/claude_code_plugin_example)

## Version History

- **1.1.0** - Added /refactor command for code refactoring
- **1.0.0** - Initial release with core commands and agents
