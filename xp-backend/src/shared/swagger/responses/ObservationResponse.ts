import { DateTime } from 'luxon';
import { Observation } from '../../../modules/observation/entities/observation.entity';
import { ApiProperty } from '@nestjs/swagger';
import { MediaGroupItemResponse } from './MediaGroupItem.response';

export class ObservationResponse implements Partial<Observation> {
  @ApiProperty()
  id: number;

  @ApiProperty({ nullable: true })
  text?: string;

  @ApiProperty({ nullable: true })
  tg_photo_id?: string;

  @ApiProperty({ nullable: true })
  tg_document_id?: string;

  @ApiProperty({ nullable: true })
  tg_voice_id?: string;

  @ApiProperty({ nullable: true })
  tg_video_id?: string;

  @ApiProperty({ nullable: true })
  tg_video_note_id?: string;

  @ApiProperty({ nullable: true })
  file_urls?: string[];

  @ApiProperty({ nullable: true, type: MediaGroupItemResponse, isArray: true })
  tg_media_group?: MediaGroupItemResponse[];

  @ApiProperty({ type: String })
  created_at: DateTime;
}
