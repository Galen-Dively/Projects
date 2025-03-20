
void main() {
    unsigned short *video_memory = (unsigned short*)0xB8000;

    video_memory[0] = 0x0748;
    video_memory[1] = 0x0769;

}
