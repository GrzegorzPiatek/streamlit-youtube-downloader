from components import *

def main():
    load_components()
    
def load_components():
    init()
    link_bar_container()
    video_title()
    if st.session_state.get('load_video'):
        load_video()
if __name__ == '__main__':
    main()