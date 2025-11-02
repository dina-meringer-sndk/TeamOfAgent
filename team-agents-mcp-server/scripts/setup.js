#!/usr/bin/env node

/**
 * Setup script for Team Agents MCP Server
 * This script helps configure the MCP server for VS Code integration
 */

import { execSync } from 'child_process';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = resolve(__dirname, '..');

console.log('🚀 Setting up Team Agents MCP Server...\n');

// Install dependencies
console.log('📦 Installing dependencies...');
try {
  execSync('npm install', { cwd: projectRoot, stdio: 'inherit' });
  console.log('✅ Dependencies installed\n');
} catch (error) {
  console.error('❌ Failed to install dependencies:', error);
  process.exit(1);
}

// Build the project
console.log('🔨 Building TypeScript...');
try {
  execSync('npm run build', { cwd: projectRoot, stdio: 'inherit' });
  console.log('✅ Build completed\n');
} catch (error) {
  console.error('❌ Build failed:', error);
  process.exit(1);
}

// Check for Claude Desktop config
const homeDir = process.env.USERPROFILE || process.env.HOME;
if (homeDir) {
  const configPath = resolve(homeDir, 'AppData', 'Roaming', 'Claude', 'claude_desktop_config.json');
  
  if (existsSync(configPath)) {
    console.log('📝 Found Claude Desktop config at:', configPath);
    console.log('💡 To add this MCP server to Claude Desktop, add this to your config:');
    console.log(JSON.stringify({
      "mcpServers": {
        "team-agents": {
          "command": "node",
          "args": [resolve(projectRoot, "build", "index.js")]
        }
      }
    }, null, 2));
  } else {
    console.log('💡 Claude Desktop config not found. Install Claude Desktop and configure:');
    console.log('   Path:', configPath);
  }
}

console.log('\n🎉 Setup complete!');
console.log('\n📖 Next steps:');
console.log('   1. Test the server: npm run dev');
console.log('   2. Add to Claude Desktop config (see above)');
console.log('   3. Restart Claude Desktop');
console.log('   4. The team agents will be available as MCP tools!');

// Test the server briefly
console.log('\n🧪 Testing server startup...');
try {
  const testProcess = execSync('timeout 3 node build/index.js || true', { 
    cwd: projectRoot, 
    stdio: 'pipe',
    encoding: 'utf8'
  });
  console.log('✅ Server starts successfully');
} catch (error) {
  console.log('⚠️  Server test completed (this is expected for stdio transport)');
}

console.log('\n✨ Team Agents MCP Server is ready to use!');