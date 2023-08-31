import { IsInt } from 'class-validator';

export class ProfileIdDTO {
  @IsInt()
  user_id: number;
}
