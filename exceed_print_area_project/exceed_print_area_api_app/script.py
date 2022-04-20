import fitz

#file_path = "./TRSL1589-ms.pdf"

def check_out_of_bounds(file_path):

    faulty_pages = []

    doc = fitz.open(file_path)
    
    num_pages = doc.page_count
    
    margin_size = 24
    
    for page_no in range(num_pages):
    
        is_outside = False
        
        page = doc.load_page(page_no)
    
        x0,y0,x1,y1 = page.MediaBox
    
        initial_crop_box = fitz.Rect(x0,y0,x1,y1)
    
        top_coords = fitz.Rect(x0,y0,x1,margin_size)
    
        bottom_coords = fitz.Rect(x0,y1-margin_size,x1,y1)
    
        left_coords = fitz.Rect(x0,y0,margin_size,y1)
    
        right_coords = fitz.Rect(x1-margin_size,y0,x1,y1)
    
        coords_list = [top_coords, bottom_coords, left_coords, right_coords]
        
        for coords_ in coords_list:
    #         print(coords_)
            page.set_cropbox(coords_)
    
            pix=page.get_pixmap()
    
            pix_width = pix.width
    
            pix_height = pix.height
    
            for x in range(pix_width):
    
                for y in range(pix_height):
    
                    pixel_val = pix.pixel(x,y)
            #         print(pixel_val)
                    if (pixel_val != (255,255,255)):
    #                     print(pixel_val)
                        is_outside = True
                        
            page.set_cropbox(initial_crop_box)
        
        if is_outside:
            faulty_pages.append(page_no + 1)
            #print("Page Number:- ",page_no + 1)

    return faulty_pages


#check_out_of_bounds(file_path)