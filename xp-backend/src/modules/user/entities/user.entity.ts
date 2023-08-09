import { Experiment } from 'src/modules/experiment/entities/experiment.entity';
import { Observation } from 'src/modules/observation/entities/observation.entity';
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  Index,
  OneToMany,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column('bigint', { nullable: true, unique: true })
  tg_id: number;

  @Column('varchar', { length: 32, nullable: true, unique: true })
  username: string;

  @Index()
  @CreateDateColumn({ select: false, type: 'timestamptz' })
  created_at: Date;

  @Index()
  @DeleteDateColumn({ select: false, type: 'timestamptz' })
  deleted_at: Date;

  @OneToMany(() => Observation, (entity) => entity.user)
  observations: Observation[];

  @OneToMany(() => Experiment, (entity) => entity.user)
  experiments: Observation[];
}
