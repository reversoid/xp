import { IsOptional, IsString } from 'class-validator';

export class MediaGroupDTO {
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
