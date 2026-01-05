from PIL import Image
import os

# Configurações
input_folder = "etc/Upscalling"
output_folder = "etc/90x90"
target_size = (90, 90)

# Criar pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Processar todas as imagens
files_processed = []
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        
        # Abrir imagem
        img = Image.open(input_path)
        
        # Redimensionar com LANCZOS (alta qualidade)
        img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
        
        # Salvar com qualidade máxima
        output_filename = os.path.splitext(filename)[0] + '_90x90.png'
        output_path = os.path.join(output_folder, output_filename)
        
        if img_resized.mode == 'RGBA':
            img_resized.save(output_path, 'PNG', optimize=True, quality=100)
        else:
            img_resized.save(output_path, 'PNG', optimize=True)
        
        files_processed.append(output_filename)
        print(f"✓ {filename} → {output_filename}")

print(f"\n✅ Total processado: {len(files_processed)} arquivos")
print(f"📁 Pasta de saída: {output_folder}")
