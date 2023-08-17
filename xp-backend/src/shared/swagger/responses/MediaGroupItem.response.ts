import { ApiProperty } from '@nestjs/swagger';
import { MediaGroupItem } from 'src/shared/types/Media-group-item.type';

export class MediaGroupItemResponse implements MediaGroupItem {
  @ApiProperty({ nullable: true })
  audio_id?: string;

  @ApiProperty({ nullable: true })
  document_id?: string;

  @ApiProperty({ nullable: true })
  photo_id?: string;

  @ApiProperty({ nullable: true })
  video_id?: string;
}
