import os
import base64
from pathlib import Path

def convert_image_to_base64(image_path):
    """Converte uma imagem para base64"""
    with open(image_path, 'rb') as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded

def get_mime_type(filename):
    """Retorna o MIME type baseado na extensão do arquivo"""
    ext = filename.lower().split('.')[-1]
    mime_types = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'svg': 'image/svg+xml',
        'gif': 'image/gif'
    }
    return mime_types.get(ext, 'image/png')

def main():
    # Criar pasta de saída
    output_dir = "etc/base64"
    os.makedirs(output_dir, exist_ok=True)
    
    # Pastas de imagens para processar
    image_folders = {
        "etc/Remove BG/1400x1400": "fotos_profissionais",
        "etc/Upscalling": "logos",
        "etc/90x90": "imagens_90x90",
        ".": "icones"  # Para os ícones na raiz
    }
    
    print("🔄 Convertendo imagens para Base64...\n")
    
    total_converted = 0
    
    for folder, prefix in image_folders.items():
        if not os.path.exists(folder):
            continue
            
        # Listar arquivos de imagem
        for filename in os.listdir(folder):
            # Pular se não for imagem
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
                continue
            
            # Caminho completo
            image_path = os.path.join(folder, filename)
            
            # Pular se for diretório
            if os.path.isdir(image_path):
                continue
            
            try:
                # Converter para base64
                base64_string = convert_image_to_base64(image_path)
                mime_type = get_mime_type(filename)
                
                # Nome do arquivo de saída
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{prefix}_{base_name}.txt"
                output_path = os.path.join(output_dir, output_filename)
                
                # Salvar em arquivo de texto
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("=" * 80 + "\n")
                    f.write(f"IMAGEM: {filename}\n")
                    f.write(f"PASTA: {folder}\n")
                    f.write(f"MIME TYPE: {mime_type}\n")
                    f.write("=" * 80 + "\n\n")
                    f.write("CÓDIGO COMPLETO PARA HTML (copie e cole no src):\n")
                    f.write("-" * 80 + "\n")
                    f.write(f"data:{mime_type};base64,{base64_string}\n")
                    f.write("-" * 80 + "\n\n")
                    f.write("APENAS O BASE64 (sem data URI):\n")
                    f.write("-" * 80 + "\n")
                    f.write(base64_string + "\n")
                    f.write("-" * 80 + "\n")
                
                print(f"✅ {filename} → {output_filename}")
                total_converted += 1
                
            except Exception as e:
                print(f"❌ Erro ao processar {filename}: {e}")
    
    print(f"\n{'='*80}")
    print(f"✅ CONCLUÍDO!")
    print(f"📁 Total de imagens convertidas: {total_converted}")
    print(f"📂 Pasta de saída: {output_dir}")
    print(f"{'='*80}")
    
    # Criar README
    readme_path = os.path.join(output_dir, "README.txt")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("CÓDIGOS BASE64 DAS IMAGENS - ASSINATURA DE EMAIL\n")
        f.write("=" * 80 + "\n\n")
        f.write("COMO USAR:\n")
        f.write("-" * 80 + "\n")
        f.write("1. Abra o arquivo .txt correspondente à imagem que deseja usar\n")
        f.write("2. Copie o 'CÓDIGO COMPLETO PARA HTML'\n")
        f.write("3. Cole diretamente no atributo src da tag <img> no HTML\n\n")
        f.write("EXEMPLO:\n")
        f.write("-" * 80 + "\n")
        f.write('<img src="data:image/png;base64,iVBORw0KG...">\n\n')
        f.write("ORGANIZAÇÃO DOS ARQUIVOS:\n")
        f.write("-" * 80 + "\n")
        f.write("• fotos_profissionais_* = Fotos de colaboradores (1400x1400)\n")
        f.write("• logos_* = Logos das empresas (upscalling)\n")
        f.write("• imagens_90x90_* = Imagens redimensionadas para 90x90px\n")
        f.write("• icones_* = Ícones (outlook, whatsapp, location, etc)\n\n")
        f.write("=" * 80 + "\n")
    
    print(f"\n📄 README criado em: {readme_path}\n")

if __name__ == "__main__":
    main()
