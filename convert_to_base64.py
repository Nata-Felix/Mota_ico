import os
import re
import base64
import urllib.request
from pathlib import Path

def download_and_encode_image(url):
    """Baixa uma imagem e retorna em base64"""
    try:
        print(f"  Baixando: {url}")
        with urllib.request.urlopen(url) as response:
            image_data = response.read()
            
        # Detectar tipo de imagem pela extensão
        if url.lower().endswith('.png'):
            mime_type = 'image/png'
        elif url.lower().endswith(('.jpg', '.jpeg')):
            mime_type = 'image/jpeg'
        elif url.lower().endswith('.svg'):
            mime_type = 'image/svg+xml'
        else:
            mime_type = 'image/png'
        
        # Converter para base64
        base64_data = base64.b64encode(image_data).decode('utf-8')
        return f"data:{mime_type};base64,{base64_data}"
    except Exception as e:
        print(f"  ❌ Erro ao baixar {url}: {e}")
        return None

def convert_html_to_base64(input_file, output_file):
    """Converte um HTML com URLs de imagens para base64"""
    print(f"\n📄 Processando: {os.path.basename(input_file)}")
    
    # Ler HTML
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Encontrar todas as tags img com src
    img_pattern = r'<img\s+[^>]*src="([^"]+)"[^>]*>'
    matches = re.finditer(img_pattern, html_content, re.IGNORECASE)
    
    urls_converted = []
    for match in matches:
        full_tag = match.group(0)
        original_url = match.group(1)
        
        # Pular se já for base64
        if original_url.startswith('data:'):
            continue
        
        # Baixar e converter
        base64_url = download_and_encode_image(original_url)
        
        if base64_url:
            # Substituir URL por base64
            new_tag = full_tag.replace(f'src="{original_url}"', f'src="{base64_url}"')
            html_content = html_content.replace(full_tag, new_tag)
            urls_converted.append(original_url)
    
    # Salvar arquivo convertido
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"  ✅ Convertidas {len(urls_converted)} imagens")
    return len(urls_converted)

def main():
    # Configurações
    input_dir = "Aprovadas"
    output_dir = "Aprovadas/offline"
    
    # Criar pasta de saída
    os.makedirs(output_dir, exist_ok=True)
    
    # Processar todos os arquivos HTML
    total_files = 0
    total_images = 0
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.html'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            images_converted = convert_html_to_base64(input_path, output_path)
            total_files += 1
            total_images += images_converted
    
    print(f"\n{'='*50}")
    print(f"✅ CONCLUÍDO!")
    print(f"📁 Arquivos processados: {total_files}")
    print(f"🖼️ Imagens convertidas: {total_images}")
    print(f"📂 Pasta de saída: {output_dir}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
