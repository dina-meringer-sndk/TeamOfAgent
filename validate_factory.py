import os

def validate_agents_factory():
    print("🏭 Agents Factory Validation Report")
    print("=" * 50)
    
    # Check core structure
    required_dirs = [
        ".bmad-core/agents",
        ".bmad-core/tasks", 
        ".bmad-core/templates",
        ".bmad-core/commands",
        ".bmad-core/checklists",
        ".bmad-core/data",
        ".bmad-core/utils",
        "output"
    ]
    
    print("📁 Directory Structure:")
    all_dirs_exist = True
    for directory in required_dirs:
        exists = os.path.exists(directory)
        status = "✅" if exists else "❌"
        print(f"  {status} {directory}")
        if not exists:
            all_dirs_exist = False
    
    # Check key files
    required_files = [
        ".bmad-core/agents/agents_factory.prompt.md",
        ".bmad-core/tasks/create-agent.md",
        ".bmad-core/tasks/revise-agent.md",
        ".bmad-core/templates/agent-summary-tmpl.md",
        ".bmad-core/templates/agent-summary-tmpl.docx",
        ".bmad-core/utils/docx_utils.py",
        "README.md",
        "QUICK_START.md"
    ]
    
    print("\n📄 Core Files:")
    all_files_exist = True
    for filepath in required_files:
        exists = os.path.exists(filepath)
        status = "✅" if exists else "❌"
        print(f"  {status} {filepath}")
        if not exists:
            all_files_exist = False
    
    # Check commands
    command_files = ["help.md", "create.md", "revise.md", "list-agents.md", "doc-out.md", "exit.md"]
    
    print("\n⚡ Command Definitions:")
    all_commands_exist = True
    for cmd_file in command_files:
        filepath = f".bmad-core/commands/{cmd_file}"
        exists = os.path.exists(filepath)
        status = "✅" if exists else "❌"
        print(f"  {status} {cmd_file}")
        if not exists:
            all_commands_exist = False
    
    print("\n🎯 Summary:")
    if all_dirs_exist and all_files_exist and all_commands_exist:
        print("✅ Agents Factory is COMPLETE and ready to use!")
        print("\n🚀 Quick Start:")
        print("1. Load: .bmad-core/agents/agents_factory.prompt.md")
        print("2. Type: *help to see available commands")
        print("3. Type: *create to start building agents")
    else:
        print("❌ Some components are missing. Please check the failed items above.")

if __name__ == "__main__":
    validate_agents_factory()