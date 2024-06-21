import os
import cairosvg

def convert_svg_to_png(svg_file_path, png_file_path):
    """Convert an SVG file to PNG format."""
    cairosvg.svg2png(url=svg_file_path, write_to=png_file_path)

def convert_folder_of_svgs_to_pngs(svg_folder_path, png_folder_path):
    """Convert all SVG files in a folder to PNG format."""
    if not os.path.exists(png_folder_path):
        os.makedirs(png_folder_path)

    for svg_file_name in os.listdir(svg_folder_path):
        if svg_file_name.endswith(".svg"):
            svg_file_path = os.path.join(svg_folder_path, svg_file_name)
            png_file_name = svg_file_name.replace(".svg", ".png")
            png_file_path = os.path.join(png_folder_path, png_file_name)
            convert_svg_to_png(svg_file_path, png_file_path)
            print(f"Converted {svg_file_path} to {png_file_path}")

# Example usage
svg_folder_path = "udifry\assets\vectorso"
png_folder_path = "udifry\assets\vectors"
convert_folder_of_svgs_to_pngs(svg_folder_path, png_folder_path)