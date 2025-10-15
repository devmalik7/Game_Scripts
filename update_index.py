#!/usr/bin/env python3

import os
import re
from pathlib import Path

def get_game_description(game_path):
    readme_path = os.path.join(game_path, 'README.md')
    if os.path.exists(readme_path):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#') and len(line) > 10:
                        clean_line = re.sub(r'[*_`]', '', line)
                        return clean_line
        except:
            pass
    
    for file in os.listdir(game_path):
        if file.lower().endswith(('.py', '.js', '.java', '.cpp')):
            try:
                with open(os.path.join(game_path, file), 'r', encoding='utf-8') as f:
                    content = f.read(1000)
                    lines = content.split('\n')[:15]
                    for line in lines:
                        line = line.strip()
                        if line.startswith('#'):
                            desc = line[1:].strip()
                            if len(desc) > 10 and not any(word in desc.lower() for word in 
                                ['!/usr/bin/env', 'coding:', 'author:', 'date:', 'copyright']):
                                return desc
                        elif line.startswith('//'):
                            desc = line[2:].strip()
                            if len(desc) > 10 and 'license' not in desc.lower():
                                return desc
                        elif '/*' in line or line.startswith('*'):
                            desc = re.sub(r'/\*|\*/|\*', '', line).strip()
                            if len(desc) > 10:
                                return desc
            except:
                continue
    
    return "A fun game built with core programming concepts"

def scan_games():
    languages = ['Python', 'java', 'javascript']
    games = {}
    
    for lang in languages:
        if os.path.exists(lang):
            games[lang] = []
            for item in os.listdir(lang):
                item_path = os.path.join(lang, item)
                if os.path.isdir(item_path):
                    description = get_game_description(item_path)
                    games[lang].append({
                        'name': item,
                        'path': f"./{item_path}",
                        'description': description
                    })
    
    return games

def generate_index(games):
    content = []
    content.append("# 🎮 Game Scripts Index")
    content.append("")
    content.append("Welcome to Game_Scripts — an open-source collection of mini games!")
    content.append("This index automatically tracks all games across different programming languages.")
    content.append(f"Last updated: {os.popen('date').read().strip() if os.name != 'nt' else 'N/A'}")
    content.append("")
    
    content.append("## 📚 Table of Contents")
    for lang in sorted(games.keys()):
        if games[lang]:
            content.append(f"- [{lang.title()}](#{lang.lower()}-games)")
    
    content.append("")
    
    for lang in sorted(games.keys()):
        if games[lang]:
            content.append(f"## 🐍 {lang.title()} Games")
            content.append("")
            
            for game in sorted(games[lang], key=lambda x: x['name'].lower()):
                content.append(f"### 🎯 [{game['name']}]({game['path']}/)")
                content.append(f"{game['description']}")
                content.append("")
    
    return "\n".join(content)

def main():
    print("🔍 Scanning for games...")
    games = scan_games()
    
    print("📝 Generating INDEX.md...")
    index_content = generate_index(games)
    
    with open('INDEX.md', 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    total_games = sum(len(v) for v in games.values())
    print(f"✅ INDEX.md updated successfully!")
    print(f"📊 Tracked {total_games} games across {len(games)} languages.")
    
    if total_games > 0:
        print("\n📋 Games found:")
        for lang, game_list in games.items():
            if game_list:
                print(f"  {lang.title()}: {len(game_list)} games")
                for game in game_list[:3]:
                    print(f"    - {game['name']}")
                if len(game_list) > 3:
                    print(f"    ... and {len(game_list) - 3} more")

if __name__ == "__main__":
    main()
