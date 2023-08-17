import { DateTime } from 'luxon';
import { Observation } from 'src/modules/observation/entities/observation.entity';
import { Geo } from 'src/shared/types/Geo.type';
import { ApiProperty } from '@nestjs/swagger';
import {
  Experiment,
  ExperimentStatus,
} from 'src/modules/experiment/entities/experiment.entity';
import { MediaGroupItemResponse } from './MediaGroupItem.response';

export class ExperimentResponse implements Partial<Experiment> {
  @ApiProperty()
  id: number;

  @ApiProperty({ nullable: true })
  text?: string;

  @ApiProperty({ nullable: true })
  tg_photo_id?: string;

  @ApiProperty({ nullable: true })
  tg_video_id?: string;

  @ApiProperty({ nullable: true })
  tg_video_note_id?: string;

  @ApiProperty({ nullable: true })
  tg_voice_id?: string;

  @ApiProperty({ nullable: true })
  tg_document_id?: string;

  @ApiProperty({ nullable: true, type: MediaGroupItemResponse })
  tg_media_group?: MediaGroupItemResponse[];

  @ApiProperty({ nullable: true })
  geo?: Geo;

  @ApiProperty({ enum: ExperimentStatus })
  status: ExperimentStatus;

  @ApiProperty({ nullable: true })
  completed_at?: DateTime;

  @ApiProperty()
  complete_by: DateTime;

  @ApiProperty()
  observations: Observation[];

  @ApiProperty({ type: String })
  created_at: DateTime;
}
