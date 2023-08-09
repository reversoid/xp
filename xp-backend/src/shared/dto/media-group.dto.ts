import { IsOptional, IsString } from 'class-validator';
import { MediaGroupItem } from '../types/Media-group-item.type';

export class MediaGroupDTO implements MediaGroupItem {
  @IsOptional()
  @IsString()
  audio_id: string;

  @IsOptional()
  @IsString()
  document_id: string;

  @IsOptional()
  @IsString()
  photo_id: string;

  @IsOptional()
  @IsString()
  video_id: string;
}
