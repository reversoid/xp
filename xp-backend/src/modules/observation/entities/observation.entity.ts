import { User } from 'src/modules/user/entities/user.entity';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  ManyToOne,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class Observation {
  @PrimaryGeneratedColumn()
  id: number;

  @ManyToOne(() => User, (user) => user.observations, {
    nullable: false,
    onDelete: 'CASCADE',
  })
  user: User;

  @Column('text', { nullable: true })
  text?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_photo_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_document_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_voice_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_id?: string;

  @Column('varchar', { nullable: true, length: 256 })
  tg_video_note_id?: string;

  @Column('varchar', { nullable: true, length: 256, array: true })
  file_urls?: string[];

  @Index()
  @CreateDateColumn({ select: false, type: 'timestamptz' })
  created_at: Date;

  @Index()
  @DeleteDateColumn({ select: false, type: 'timestamptz' })
  deleted_at: Date;
}
