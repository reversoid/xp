import { User } from 'src/modules/user/entities/user.entity';
import { Geo } from 'src/shared/types/Geo.type';
import { MediaGroupItem } from 'src/shared/types/Media-group-item.type';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  ManyToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';

export enum ExperimentStatus {
  STARTED = 'STARTED',
  COMPLETED = 'COMPLETED',
  CANCELED = 'CANCELED',
}

@Entity()
export class Experiment {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @Column('text', { nullable: false })
  text: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_photo_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_note_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_voice_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_document_id?: string;

  @Column('jsonb', { nullable: true, array: true })
  tg_media_group?: MediaGroupItem[];

  @Column('jsonb', { nullable: true })
  geo?: Geo;

  @Column('enum', {
    enum: ExperimentStatus,
    default: ExperimentStatus.STARTED,
    nullable: false,
  })
  status: ExperimentStatus;

  @Column('timestamptz', { nullable: true })
  completed_at?: number;

  @Column('timestamptz', { nullable: false })
  complete_by: Date;

  @Index()
  @CreateDateColumn({ select: false, type: 'timestamptz' })
  created_at: Date;

  @Index()
  @DeleteDateColumn({ select: false, type: 'timestamptz' })
  deleted_at: Date;
}
