# Complete Guide to Creating and Sharing Claude Code Plugins

## What Are Claude Code Plugins?

Claude Code plugins are a powerful way to package and share custom configurations including:
- **Slash commands**: Custom shortcuts for frequently-used operations
- **Subagents**: Purpose-built agents for specialized tasks
- **Guidelines**: Development standards and best practices (CLAUDE.md)
- **Hooks**: Custom workflow automation
- **MCP servers**: Tool and data source integrations

Plugins work seamlessly across terminal and VS Code environments.

## Why Create Plugins?

- **Team Standardization**: Share consistent workflows and coding standards
- **Open Source Support**: Help contributors use your project correctly
- **Workflow Automation**: Distribute debugging setups and deployment pipelines
- **Knowledge Sharing**: Package your expertise into reusable tools

## Creating Your First Plugin

### Step 1: Initialize the Plugin Structure

Create the following directory structure:

```bash
my-plugin/
├── .claude-plugin/
│   ├── plugin.json          # Required: Plugin manifest
│   └── marketplace.json     # Optional: For distribution
├── commands/                 # Slash commands (.md files)
├── agents/                   # Custom agents (.json files)
├── hooks/                    # Hook configurations
│   └── hooks.json
├── CLAUDE.md                 # Optional: Guidelines
└── README.md                 # Documentation
```

### Step 2: Create the Plugin Manifest

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description of your plugin",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/yourusername"
  },
  "homepage": "https://github.com/yourusername/my-plugin",
  "repository": "https://github.com/yourusername/my-plugin",
  "license": "MIT",
  "keywords": [
    "keyword1",
    "keyword2"
  ]
}
```

**Required fields:**
- `name`: Unique identifier (kebab-case)
- Other fields are optional but recommended

### Step 3: Add Slash Commands

Create markdown files in the `commands/` directory. Each file becomes a slash command.

Example: `commands/review.md`

```markdown
You are performing a code review. Please analyze the code and provide:

1. **Code Quality Assessment**
   - Readability and maintainability
   - Adherence to best practices

2. **Security Concerns**
   - Vulnerability assessment
   - Input validation issues

3. **Performance Considerations**
   - Optimization opportunities

Provide specific, actionable feedback with examples.
```

The filename determines the command name. `review.md` becomes `/review`.

### Step 4: Create Custom Agents

Create JSON files in the `agents/` directory:

Example: `agents/debugging-agent.json`

```json
{
  "name": "debugging-agent",
  "description": "Specialized agent for debugging code issues",
  "systemPrompt": "You are a debugging specialist. Your goal is to:\n\n1. Analyze error messages thoroughly\n2. Identify root causes\n3. Provide step-by-step solutions\n\nProvide clear, actionable solutions with explanations.",
  "tools": ["Read", "Grep", "Bash", "Edit", "Write"]
}
```

### Step 5: Add Development Guidelines

Create `CLAUDE.md` with your team's coding standards:

```markdown
# Development Guidelines

## Code Quality Standards
- Write clean, readable code
- Follow SOLID principles
- Keep functions small and focused

## Testing Requirements
- Aim for 80%+ test coverage
- Write tests alongside implementation
- Test edge cases

## Security Best Practices
- Validate all user inputs
- Use parameterized queries
- Store passwords securely
```

## Sharing Your Plugin

### Option 1: GitHub/GitLab Repository (Recommended)

1. **Initialize Git and push to remote:**

```bash
git init
git add .
git commit -m "Initial plugin release"
git remote add origin https://github.com/yourusername/my-plugin.git
git push -u origin master
```

2. **Create marketplace configuration** (`.claude-plugin/marketplace.json`):

```json
{
  "name": "my-marketplace",
  "description": "Curated collection of development tools",
  "version": "1.0.0",
  "owner": {
    "name": "Your Name",
    "email": "[email protected]"
  },
  "author": {
    "name": "Your Name",
    "url": "https://github.com/yourusername"
  },
  "plugins": [
    {
      "name": "my-plugin",
      "version": "1.0.0",
      "description": "Brief description",
      "source": "./",
      "author": {
        "name": "Your Name"
      },
      "keywords": ["keyword1", "keyword2"]
    }
  ]
}
```

**Important:**
- `owner` must be an object with `name` and `email`
- `source` must start with `./`

3. **Users can install with:**

```bash
/plugin marketplace add yourusername/my-plugin
/plugin install my-plugin
```

### Option 2: Private Git Repository

Works with any Git hosting (GitLab, Bitbucket, private servers):

```bash
# Users with access can install via:
/plugin marketplace add git@your-server.com:username/plugin.git
/plugin install my-plugin

# Or clone first and add locally:
git clone https://your-server.com/username/plugin.git
/plugin marketplace add /path/to/plugin
/plugin install my-plugin
```

### Option 3: Local Distribution

Share the plugin directory directly:

```bash
# Users add it as a local marketplace:
/plugin marketplace add /path/to/plugin
/plugin install my-plugin
```

## Using Plugins

### Installation

```bash
# Add marketplace
/plugin marketplace add username/repo-name

# Install specific plugin
/plugin install plugin-name

# Or install from marketplace
/plugin install plugin-name@marketplace-name
```

### Using Slash Commands

Once installed, slash commands are available immediately:

```bash
/review              # Run code review
/test-plan          # Generate test plan
/docs               # Create documentation
```

### Using Custom Agents

Agents work automatically when relevant, or can be invoked explicitly through natural language:

```
"Debug the authentication error I'm seeing"
"Write comprehensive tests for the user service"
"Refactor this code to improve maintainability"
```

### Managing Plugins

```bash
# List installed plugins
/plugin list

# Disable a plugin
/plugin disable plugin-name

# Enable a plugin
/plugin enable plugin-name

# Uninstall a plugin
/plugin uninstall plugin-name
```

## Updating Your Plugin

### For Plugin Authors

1. **Make your changes** (add commands, update agents, etc.)

2. **Update version numbers:**

```json
// .claude-plugin/plugin.json
{
  "version": "1.1.0"  // Increment version
}

// .claude-plugin/marketplace.json
{
  "version": "1.1.0",
  "plugins": [
    {
      "version": "1.1.0"  // Update here too
    }
  ]
}
```

3. **Commit and push:**

```bash
git add .
git commit -m "Release version 1.1.0: Add new features"
git push origin master
```

### For Plugin Users

To upgrade to the latest version:

```bash
# Uninstall current version
/plugin uninstall plugin-name

# Reinstall to get latest
/plugin install plugin-name@marketplace-name
```

## Best Practices

### Command Design

1. **Be specific**: Clear, focused prompts work better than generic ones
2. **Provide structure**: Use numbered lists and sections
3. **Include examples**: Show what good output looks like
4. **Set constraints**: Define what to avoid or exclude

### Agent Design

1. **Single responsibility**: Each agent should have one clear purpose
2. **Detailed system prompt**: Explain the agent's role and approach
3. **Appropriate tools**: Only include tools the agent needs
4. **Clear descriptions**: Help users understand when to use each agent

### Guidelines (CLAUDE.md)

1. **Be prescriptive**: Clear rules, not suggestions
2. **Provide examples**: Show good vs bad patterns
3. **Keep updated**: Review and update regularly
4. **Team alignment**: Ensure team buy-in on standards

### Versioning

Follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

## Debugging Plugins

If your plugin isn't working:

1. **Check plugin loading:**

```bash
claude --debug
```

This shows plugin loading details and manifest errors.

2. **Validate JSON syntax:**

Ensure all JSON files are valid:
- No trailing commas
- Proper quote escaping
- Matching braces

3. **Check file paths:**

- Commands: `commands/*.md`
- Agents: `agents/*.json`
- Source path must start with `./` in marketplace.json

4. **Verify permissions:**

Ensure files are readable and in the correct locations.

## Example Plugin Structure

Here's a complete example:

```
dev-tools/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── commands/
│   ├── review.md
│   ├── test.md
│   └── deploy.md
├── agents/
│   ├── debugger.json
│   └── tester.json
├── hooks/
│   └── hooks.json
├── CLAUDE.md
└── README.md
```

## Real-World Example

Check out this complete example plugin:

- **Repository**: [androidyue/claude_code_plugin_example](https://github.com/androidyue/claude_code_plugin_example)
- **Installation**: `/plugin marketplace add androidyue/claude_code_plugin_example`

It includes:
- 6 slash commands (review, test-plan, docs, optimize, refactor, commit)
- 4 specialized agents (debugging, testing, refactoring, security)
- Comprehensive development guidelines
- Full documentation

## Advanced Topics

### Combining Multiple Plugins

Users can install multiple plugins simultaneously. Commands and agents from all enabled plugins are available.

### Private Marketplaces

Create internal marketplaces for your organization:

1. Host plugin repositories on private Git servers
2. Share marketplace URLs within your team
3. Control access via Git permissions

### Custom Hooks

Add workflow automation by creating `hooks/hooks.json`:

```json
{
  "pre-commit": "echo 'Running pre-commit checks...'",
  "post-commit": "echo 'Commit successful!'"
}
```

### MCP Server Integration

Connect external tools via `.mcp.json`:

```json
{
  "mcpServers": {
    "my-tool": {
      "command": "node",
      "args": ["server.js"]
    }
  }
}
```

## Resources

- **Documentation**: [Claude Code Plugins Docs](https://docs.claude.com/en/docs/claude-code/plugins)
- **Plugin Reference**: [Plugins Reference](https://docs.claude.com/en/docs/claude-code/plugins-reference)
- **Marketplace Guide**: [Plugin Marketplaces](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- **Announcement**: [Claude Code Plugins Launch](https://www.anthropic.com/news/claude-code-plugins)

## Conclusion

Claude Code plugins enable you to package expertise, standardize workflows, and share best practices across teams and projects. Start by creating a simple plugin with a few commands, then expand based on your team's needs.

The plugin system is flexible and powerful - use it to capture your team's knowledge and make it accessible to everyone.

Happy plugin building!
